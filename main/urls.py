from django.urls import path
from sqlparse.filters import output

import music
from .views import *
from music.views import get_audio
from .views import search_results
app_name = 'main'
urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('input/', input),
    path('home/', home),
    path('get-audio/<int:audio_id>/', views.get_audio, name='get_audio'),
    path('search_results/', views.search_results, name='search_results'),
    path('personal_account/',views.personal_account, name='personal_account'),
]
