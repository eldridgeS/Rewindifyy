from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.urls import path
import requests
import json
from Rewindify.settings import SPOTIFY_REDIRECT_URI, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def home(request):
    return render(request, 'myappp/home.html')
def signup(request):
    return render(request, 'myappp/signup.html')





def login_spotify(request):
    scope = 'playlist-read-private playlist-read-collaborative user-read-playback-state user-modify-playback-state'
    auth_url = f"https://accounts.spotify.com/authorize?response_type=code&client_id={SPOTIFY_CLIENT_ID}&redirect_uri={SPOTIFY_REDIRECT_URI}&scope={scope}"
    return redirect(auth_url)


def callback_spotify(request):
    code = request.GET.get('code')
    if not code:
        return render(request, 'myappp/error.html', {'error': 'No authorization code returned.'})

    token_url = 'https://accounts.spotify.com/api/token'
    response = requests.post(token_url, {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    })

    token_data = response.json()
    if 'error' in token_data:
        return render(request, 'myappp/error.html', {'error': token_data['error_description']})

    request.session['access_token'] = token_data.get('access_token')
    return redirect('playlists')  # Ensure this matches the URL name defined above

def view_playlists(request):
    access_token = request.session.get('access_token')
    if access_token:
        headers = {'Authorization': f'Bearer {access_token}'}
        playlists_response = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
        print(playlists_response.content)

        if playlists_response.status_code == 200:
            playlists = playlists_response.json()
            return render(request, 'myappp/user_info.html', {'playlists': playlists['items']})
        else:
            error_message = playlists_response.json().get('error', {}).get('message', 'Unknown error')
            return render(request, 'myappp/error.html', {'error': f'Error fetching playlists: {error_message}'})

    return redirect('login_spotify')




