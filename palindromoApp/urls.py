from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingreso_palabra, name='ingreso_palabra'),
]