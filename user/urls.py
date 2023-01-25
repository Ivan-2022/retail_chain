from django.urls import path
from .views import SignupView
from rest_framework.authtoken import views

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', views.obtain_auth_token, name='login'),
]
