
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls"), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
]

