from django.urls import path
from myapp4 import views
from .views import index, about, coin, cube, author_posts, post

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('coin/<int:count>/', coin, name='base_games'),
    path('cube/<int:count>/', cube, name='base_games'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post, name='posts')
]