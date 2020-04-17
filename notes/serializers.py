from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)

    class Meta:
        model = Note
        fields = '__all__'
        
        def create(self, validated_data):
            return Note.objects.create(**validated_data)