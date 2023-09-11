from django.urls import path
from myapp4 import views
from .views import index, about, coin, cube, rand_int, author_posts, post, gamer_form, author_form, post_form

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('coin/<int:count>/', coin, name='coin'),
    path('cube/<int:count>/', cube, name='cube'),
    path('rand/<int:count>/', rand_int, name='rand'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post, name='posts'),
    path('game/', gamer_form, name='game_form'),
    path('author/add/', author_form, name='author_form'),
    path('post/add/', post_form, name='post_form'),
]