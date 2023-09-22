from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('memes/', views.memes_index, name='index'),
    path('memes/<int:meme_id>/', views.meme_detail, name='detail'),
]