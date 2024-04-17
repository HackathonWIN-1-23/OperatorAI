import os
import uuid
from urllib.parse import urljoin

import requests
import json
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.http import FileResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from g4f.client import Client
from django.conf import settings

class Chat:
    def __init__(self):
        self.client = Client()
        self.chat_history = []

    def send_message(self, message):
        try:
            self.chat_history.append({"role": "user", "content": message})
            print(self.chat_history)
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.chat_history
            )
            self.chat_history.append(
                {"role": response.choices[0].message.role, "content": response.choices[0].message.content})
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

        chat_response = chat.send_message(plain_text)
        print("AI: ", chat_response)

        data = {
            "speaker_id": 2,
            "text": chat_response
        }
        url = 'https://tts.ulut.kg/api/tts'
        audio_response = requests.post(url, json=data, headers={'Authorization': f'Bearer {self.bearer_token}'})

        if response.status_code == 200:
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
            print('Произошла ошибка при отправке запроса:', response.status_code)

    def get(self, request, format=None):
        return Response({'message': 'Hello World!'})
