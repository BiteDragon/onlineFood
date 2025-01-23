from django.urls import path
from . import views

urlpatterns = [
    path('resgisterUser/',views.registerUser, name='registerUser')
]