from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

class AudioUploadParser(FileUploadParser):
    media_type = 'audio/wav'

class UploadView(APIView):
    parser_classes = [AudioUploadParser,]

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("No audio content")
        f = request.data['file']

        # process here
        content_bytes = f.read()
        size = f.size
        print(content_bytes)

        return Response(status=204)
