from django.urls import path
from audio import views

urlpatterns = [
    path('audio/', views.audio_upload),
]
