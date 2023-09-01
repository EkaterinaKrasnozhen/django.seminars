from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # по пустому пути ''
    path('about/', views.about, name='about')
]