from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='game'),
    path('result/', views.result, name='result'),
]
