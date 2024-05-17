from typing import Dict

from django.shortcuts import render, redirect
from django.urls import path
from django.http import FileResponse
from music.models import Song,Album
from music.views import get_audio  # Импортируем представление get_audio из приложения music
from . import views
from .forms import PhotoUploadForm
# Create your views here.
def home(request):
    return render(request, 'main/home2.html')

def input(request):
    return render(request, 'main/input.html')


from django.shortcuts import render



import datetime


def mainpage(request):
    query = request.GET.get('query')
    songs = []
    albums = []
    current_time = datetime.datetime.now()
    return render(request, 'main/mainpage.html', {'songs': songs, 'albums': albums, 'query': query,'current_time': current_time})


def search_results(request):
    query = request.GET.get('query')
    songs = Song.objects.filter(song_title__icontains=query)
    albums = Album.objects.filter(album_title__icontains=query)
    songs = songs[:5]
    albums = albums[:5]
    return render(request, 'main/search_results.html', {'songs': songs, 'albums': albums, 'query': query})


def personal_account(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем фотографию в профиль пользователя
            request.user.profile.photo = form.cleaned_data['photo']
            request.user.profile.save()
            return redirect('main:personal_account')
    else:
        form = PhotoUploadForm()
    return render(request, 'main/personal_account.html', {'form': form})


from django.http import JsonResponse

def current_time(request):
    import datetime
    current_time = datetime.datetime.now().strftime('%H:%M:%S')  # Форматируем время
    return JsonResponse({'current_time': current_time})


def events(request):
    return render(request, 'main/events.html')



