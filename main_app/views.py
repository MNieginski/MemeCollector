from django.shortcuts import render
from .models import Meme

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def memes_index(request):
    memes = Meme.objects.all()
    return render(request, 'memes/index.html', {
        'memes' : memes
    })

def meme_detail(request, meme_id):
    meme = Meme.objects.get(id=meme_id)
    return render(request, 'memes/detail.html', {
        'meme' : meme
    })