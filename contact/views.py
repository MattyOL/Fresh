from django.shortcuts import render
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
    return render(request, '../templates/contact/contact.html')
