from django.urls import path
from . import views

urlpatterns = [
    path('words/', views.WordListView.as_view(), name='word-list'),
    path('words/create/', views.WordCreateView.as_view(), name='word-create'),
]