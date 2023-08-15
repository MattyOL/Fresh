from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from allauth.account.views import PasswordResetView
from .forms import CustomSignupForm

@csrf_protect
def SignUpView(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set the authentication backend - move to settings.py
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        else:
            return redirect('signup2')
    else:
        form = UserCreationForm()
        return render(request, '../templates/allauth/account/signup.html', {'form': form})

    return redirect('home')

@csrf_protect
def ForgotPasswordView(request):
    if request.method == 'POST':
        print('here3')
        email = request.POST.get('email')
        try:
            print('here2')
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user:
            print('here')
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(f'/reset/{uid}/{token}/')

    # password_reset_view = PasswordResetView()
    # password_reset_view.request = request
    # # request = request.POST.get('email')
    # response = password_reset_view.post(request)
    # print(response)
    # print(response.status_code)

    # if response.status_code == status.HTTP_200_OK:
    #     return Response({'message': 'Password Reset Confirmed'})

    subject = 'Password Reset Confirmation'
    message = f'Please follow this link to reset your password: {reset_url}'
    from_email = 'noreply@example.com'  # Change to your sending email address
    recipient_list = [user.email]


    send_mail(subject, message, from_email, recipient_list)
    return redirect('home')