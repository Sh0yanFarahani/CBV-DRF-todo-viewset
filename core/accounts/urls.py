
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("accounts", include("django.contrib.auth.urls"), name='login'),
    path('accounts/register/', views.RegisterPage.as_view(), name='register'),
    path('api/v1/', include('accounts.api.v1.urls')),
]

