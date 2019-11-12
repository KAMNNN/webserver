from rest_framework import serializers
from audio.models import Audio


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'received', 'ts', 'session_id']
