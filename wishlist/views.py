
from django.shortcuts import render, redirect
from .models import Item, Wishlist
from django.contrib.auth.decorators import login_required

@login_required
def wishlist(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    items = user_wishlist.items.all()
    return render(request, '/workspace/Fresh/wishlist/templates/wishlist/wishlist.html', {'items': items})

@login_required
def add_to_wishlist(request, item_id):
    item = Item.objects.get(pk=item_id)
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    user_wishlist.items.add(item)
    return redirect('wishlist')