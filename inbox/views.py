from django.shortcuts import render


def inbox(request, exception):
    
    return render(request, "inbox/inbox.html", status=404)

    
