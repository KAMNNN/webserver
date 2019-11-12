from django.urls import re_path
from audio.views import UploadView

urlpatterns = [
    re_path(r'^audio/$', UploadView.as_view()),
]
