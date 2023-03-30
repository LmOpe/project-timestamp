from django.urls import path
from . import views

urlpatterns = [
    path('api/<int:date>/', views.time, name="time"),
    path('api/', views.time)
]