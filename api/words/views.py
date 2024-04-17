from rest_framework import generics, permissions
from .models import Word
from .serializers import WordSerializer


class WordCreateView(generics.CreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class WordListView(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    http_method_names = ['get']
