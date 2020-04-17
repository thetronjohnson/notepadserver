from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note
from rest_framework.permissions import IsAuthenticated



class NoteViewSet(viewsets.ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
