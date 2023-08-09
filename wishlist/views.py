from django.shortcuts import render, redirect
from .models import Wishlist
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404


@login_required
def wishlist(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    items = user_wishlist.items.all()
    return render(request, '/workspace/Fresh/wishlist/templates/wishlist/wishlist.html', {'items': items})


@login_required
def add_to_wishlist(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    user_wishlist.items.add(item)
    return redirect('wishlist')


def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    user_wishlist.items.remove(item)
    messages.success(request, 'Removed from your wishlist !')
    return redirect(reverse('wishlist'))


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect('wishlist')
