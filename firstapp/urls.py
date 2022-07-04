from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('scores/', views.scores, name = "scores"),
    path('about',views.about, name = "about"),
    path('form',views.form, name = "form"),
]