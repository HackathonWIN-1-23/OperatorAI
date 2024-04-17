from django.urls import path
from . import views

urlpatterns = [
    path('audio/', views.FileUploadView.as_view(), name='word-list'),
    # path('words/create/', views.WordCreateView.as_view(), name='word-create'),
]
