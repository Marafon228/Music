from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('mainpage/',views.mainpage, name='mainpage'),
    path('register/',views.register, name='register'),
    path('register_done/',views.register_done, name='register_done')
]