from audioop import reverse
from typing import Dict

from django.shortcuts import render
from django.conf.urls import *
from django.http import FileResponse
from .models import Song


def get_audio(request, audio_id):
    audio_file = Song.objects.get(pk=audio_id)
    response = FileResponse(audio_file.audio_file, content_type='audio/mpeg')
    return response

def mainpage(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    return render(request, 'main/mainpage.html', context)

