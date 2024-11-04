from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_spotify, name='login'),  # Login URL
    path('callback/', views.callback_spotify, name='callback'),
    path('playlists/', views.view_playlists, name='playlists'),
    path('signup/', views.signup, name='signup'),

]
