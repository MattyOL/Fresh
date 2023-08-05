import requests
import random
import string
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
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
    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

""" Newletters / mailchimp / ajax section"""

def generate_discount_code(length=8):
    """Generate a random alphanumeric discount code of the given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@csrf_exempt
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        discount_code = request.POST.get('discount_code')

        # Check if the email is not already subscribed
        if not Subscriber.objects.filter(email=email).exists():
            # Add the email to the local database
            Subscriber.objects.create(email=email)

            # Subscribe the email using Mailchimp API
            api_key = settings.MAILCHIMP_API_KEY
            list_id = settings.MAILCHIMP_LIST_ID
            url = f'https://us2.api.mailchimp.com/3.0/lists/{list_id}/members/'
            headers = {'Authorization': f'apikey {api_key}'}
            data = {
                'email_address': email,
                'status': 'subscribed',
                'merge_fields': {
                    'DISCOUNT_CODE': discount_code,  # Add the discount code as a merge field
                }
            }
            response = requests.post(url, json=data, headers=headers)

            # Check the API response
            if response.status_code == 200 or response.status_code == 201:
                # Generate a new discount code (you can use your own code generation logic here)
                generated_discount_code = generate_discount_code()
                # You can save the discount code in your database if you need to reference it later

                # Return a success message with the discount code (if generated)
                return JsonResponse({'message': 'Subscription successful!', 'discount_code': generated_discount_code})
            else:
                # Return an error message
                return JsonResponse({'message': 'Failed to subscribe. Please try again later.'}, status=500)
        else:
            return JsonResponse({'message': 'You are already subscribed!'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def send_email_with_discount(request):
    if request.method == 'POST':
        discount_code = request.POST.get('discount_code')
        
        # Replace the following lines with your email sending logic
        # This is just a sample to demonstrate the concept
        subject = 'Your Discount Code'
        message = f'Thank you for subscribing! Your discount code is {discount_code}.'
        from_email = 'your_email@example.com'
        to_email = 'recipient@example.com'
        send_mail(subject, message, from_email, [to_email])

        return JsonResponse({'message': 'Email sent successfully!'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)



def my_view(request):
    # Process form data and generate the discount code
    discount_code = "DISCOUNT20"  # Replace this with your generated discount code

    # Get the email address from the form data or any other source
    email = "recipient@example.com"  # Replace this with the actual recipient email address

    # Prepare the email content
    subject = "Your Discount Code"
    message = f"Dear Subscriber,\n\nThank you for subscribing to our newsletter. Here's your discount code: {discount_code}\n\nHappy shopping!\n\nBest regards,\nYour Company Name"
    from_email = "recipient@example.com"  # Replace this with your from email address

    # Send the email
    send_mail(subject, message, from_email, [email])

    # Return a JSON response to indicate success
    return JsonResponse({'success': True})