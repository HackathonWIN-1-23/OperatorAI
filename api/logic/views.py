import os
import uuid
from urllib.parse import urljoin

import requests
import json

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.http import FileResponse, JsonResponse, HttpResponse
from rest_framework.views import APIView
from g4f.client import Client
from django.conf import settings
from .models import Conversation
from .serializers import ConversationSerializer


class Chat:
    def __init__(self):
        self.client = Client()

    def send_message(self, message, conversation_id):
        try:
            conversation = Conversation.objects.filter(id=conversation_id).first()
            if not conversation:
                conversation = Conversation.objects.create()
            chat_history = ConversationSerializer(conversation).data.get('chat_history', [])
            chat_history.append({"role": "user", "content": message})
            print(chat_history)
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=chat_history
            )
            chat_history.append(
                {"role": response.choices[0].message.role, "content": response.choices[0].message.content})
            conversation.chat_history = chat_history
            conversation.save()
            print(response.choices[0].message.role)
            return response.choices[0].message.content
        except Exception as e:
            print("Ошибка при отправке сообщения:", e)
            return "Произошла ошибка при отправке сообщения"


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    post_url = "https://asr.ulut.kg/api/receive_data"
    bearer_token = '91ca2e12d4503ea5fe5a66c0c563fd92fdc0be6496e85507eb5f7e1e0c64dd62fd5414fc52febea169a6bbd97731c6303204f290d2757a127d56ba52044a31b8'

    def post(self, request, format=None):
        file_obj = request.data['audio']

        data = {
            "audio": file_obj
        }

        response = requests.post(self.post_url, files=data, headers={'Authorization': f'Bearer {self.bearer_token}'})
        print(response)
        result = response.text
        parsed_response = json.loads(result)
        plain_text = parsed_response['text']
        print(plain_text)

        chat = Chat()

        chat_response = chat.send_message(plain_text, request.data['conversation_id'])
        # chat_response = chat.send_message(text, request.data['conversation_id'])
        print("AI: ", chat_response)

        data = {
            "speaker_id": 2,
            "text": chat_response
        }
        url = 'https://tts.ulut.kg/api/tts'
        audio_response = requests.post(url, json=data, headers={'Authorization': f'Bearer {self.bearer_token}'})

        if audio_response.status_code == 200:
            mp3_data = audio_response.content
            file_name = str(uuid.uuid4()) + '.mp3'
            public_dir = os.path.join(settings.BASE_DIR, 'public')
            file_path = os.path.join(public_dir, file_name)
            with open(file_path, 'wb') as f:
                f.write(mp3_data)
            print('Файл успешно сохранен как output.mp3')
            file_url = urljoin("http://127.0.0.1:8000/public/", file_name)
            return JsonResponse({'file_url': file_url})
        else:
            print('Произошла ошибка при отправке запроса:', audio_response.status_code)

    def get(self, request, format=None):
        return Response({'message': 'Hello World!'})
