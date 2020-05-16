from django.conf import settings
from rest_framework import serializers
from .models import Chirp


MAX_CHIRP_LENGTH = settings.MAX_CHIRP_LENGTH

class ChirpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chirp
        fields = ['content']
        
    def validate_content(self, value):
        if len(value) > MAX_CHIRP_LENGTH:
            raise serializers.ValidationError("This chirp is too long")
        return value