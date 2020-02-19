#django imports
from django.urls import path

#project imports
from . import views


urlpatterns = [
    path('users/', views.users, name='users'),
    path('signUp/', views.signUp, name='signUp'),
    path('signUpResult/', views.signUpResult, name='signUpResult'),
    path('submit_info', views.submit_info, name='submit_info'),
]