from contact.models import Contact
from django.shortcuts import render
from django.views.generic import ListView


def inbox(request):
    
    return render(request, '../templates/inbox/inbox.html')


def inbox(request):
    contacts = Contact.objects.all()

    return render(request, '../templates/inbox/inbox.html', {'contacts': contacts})


    
