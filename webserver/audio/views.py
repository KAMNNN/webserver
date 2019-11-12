from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from audio.models import Audio
from audio.serializers import AudioSerializer


@api_view(['GET', 'POST'])
def audio_upload(request):
    if request.method == 'GET':
        audios = Audio.objects.all()
        serializer = AudioSerializer(audios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AudioSerializer(data=request.data)

	#  Add code here to process audio
        print('Process here!')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
