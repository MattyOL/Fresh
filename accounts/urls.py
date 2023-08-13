# accounts/urls.py
from django.urls import path

from .views import SignUpView, ForgotPasswordView


urlpatterns = [
    path("signup2/", SignUpView, name="signup2"),
    path("user_forgot_password", ForgotPasswordView, name="user_forgot_password")
]