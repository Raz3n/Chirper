from django.conf import settings
from rest_framework import serializers
from .models import Chirp


MAX_CHIRP_LENGTH = settings.MAX_CHIRP_LENGTH
CHIRP_ACTION_OPTIONS = settings.CHIRP_ACTION_OPTIONS


class ChirpActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    
    def validate_action(self, value):
        value = value.lower().strip()
        if not value in CHIRP_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for chirps.")
        return value
    
class ChirpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chirp
        fields = ['content']
        
    def validate_content(self, value):
        if len(value) > MAX_CHIRP_LENGTH:
            raise serializers.ValidationError("This chirp is too long")
        return value