# accounts/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView, ForgotPasswordView


# urlpatterns = [
#     path("signup2/", SignUpView, name="signup2"),
#     path("user_forgot_password", ForgotPasswordView, name="user_forgot_password"),
#     # path('accounts/', include('allauth.urls')),
#     # path('ForgotPasswordView/', ForgotPasswordView, name='ForgotPasswordView'),
# ]

urlpatterns = [
    # ...
    path("signup2/", SignUpView, name="signup2"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # ...
]