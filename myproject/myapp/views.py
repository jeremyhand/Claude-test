from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def home(request):
    return render(request, 'home.html')

def products(request):
    products_list = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    
    context = {
        'products': products_list,
        'cart_count': cart_count
    }
    return render(request, 'products.html', context)

def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id_str = str(product_id)
        
        if product_id_str in cart:
            cart[product_id_str] += 1
        else:
            cart[product_id_str] = 1
            
        request.session['cart'] = cart
        
        return JsonResponse({
            'success': True,
            'cart_count': sum(cart.values())
        })
    
    return JsonResponse({'success': False})
