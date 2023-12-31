from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('memes/', views.memes_index, name='index'),
    path('memes/<int:meme_id>/', views.meme_detail, name='detail'),
    path('memes/create', views.MemeCreate.as_view(), name='meme_create'),
    path('memes/<int:pk>/update/', views.MemeUpdate.as_view(), name='meme_update'),
    path('memes/<int:pk>/delete/', views.MemeDelete.as_view(), name='meme_delete'),
]