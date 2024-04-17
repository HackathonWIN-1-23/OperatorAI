import requests
import json
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    post_url = "https://asr.ulut.kg/api/receive_data"
    bearer_token = '91ca2e12d4503ea5fe5a66c0c563fd92fdc0be6496e85507eb5f7e1e0c64dd62fd5414fc52febea169a6bbd97731c6303204f290d2757a127d56ba52044a31b8'

    def post(self, request, format=None):
        file_obj = request.data['audio']
        data = {
            "audio": file_obj
        }

        try:
            response = requests.post(self.post_url, files=data,
                                     headers={'Authorization': f'Bearer {self.bearer_token}'})
            result = response.text
            print(result)
            return Response(json.loads(result), status=status.HTTP_200_OK)
        except:
            return Response({"message":"something went wrong"})

    def get(self, request, format=None):
        return Response({'message': 'Hello World!'})
