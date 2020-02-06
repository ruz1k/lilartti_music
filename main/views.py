from django.shortcuts import render, redirect, get_object_or_404
from .models import Artist

def artist(request):
	artists = Artist.objects.all()
	return render(request, 'main/playlist.html', {'artists': artists})

def artist_info(request, pk):
    artists = get_object_or_404(Artist, pk=pk)
    return render(request, 'main/artist_info.html', {'artists': artists})