from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note

class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
