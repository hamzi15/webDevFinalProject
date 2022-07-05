from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('scores/', views.scores, name = "scores"),
    path('postScore/', views.postScore, name = "postScore"),
]