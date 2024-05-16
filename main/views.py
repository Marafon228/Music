from typing import Dict

from django.shortcuts import render, redirect
from django.urls import path
from django.http import FileResponse
from music.models import Song
from music.views import get_audio  # Импортируем представление get_audio из приложения music
from . import views
from .forms import PhotoUploadForm
# Create your views here.
def home(request):
    return render(request, 'main/home2.html')

def input(request):
    return render(request, 'main/input.html')


from django.shortcuts import render


def mainpage(request):
    songs = Song.objects.all()
    return render(request, 'main/mainpage.html', )

def search_results(request):
    query = request.GET.get('query')
    songs = Song.objects.filter(song_title__icontains=query)
    return render(request, 'main/search_results.html', {'songs': songs, 'query': query})


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



from .forms import TimeForm

def my_view(request):
    if request.method == 'POST':
        form = TimeForm(request.POST)
    else:
        form = TimeForm(request.POST)

    return render(request, 'main/mainpage.html', {'form': form})




