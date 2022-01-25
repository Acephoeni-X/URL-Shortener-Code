from django.urls import path
from . import views

urlpatterns = [
    path('api/<str:protocol>/<str:url>/<str:method>/', views.index)
]