from django.urls import path,include

from django.contrib import admin
from . import views
from .views import get_audio

app_name = 'music'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('get-audio/<int:audio_id>/', get_audio, name='get_audio'),
]