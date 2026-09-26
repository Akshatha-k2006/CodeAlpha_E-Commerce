from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
from .models import Product,Order,OrderItem


def home(request):
    products = Product.objects.all()

    search_query = request.GET.get('q', '')
    difficulty = request.GET.get('difficulty', '')


    if search_query:
        products = products.filter(
            name__icontains=search_query
        )

    return render(request, 'home.html', {
        'products': products,
        'search_query': search_query,
    })

    if difficulty:
        products = products.filter(
            difficulty=difficulty
        )

    return render(request, 'home.html', {
        'products': products,
        'search_query': search_query,
        'selected_difficulty': difficulty,
    })

    if sort_by == 'price_low':
        products = products.order_by('price')

    elif sort_by == 'price_high':
        products = products.order_by('-price')

    elif sort_by == 'name':
        products = products.order_by('name')


    return render(request, 'home.html', {
        'products': products,
        'search_query': search_query,
        'selected_difficulty': difficulty,
        'selected_sort': sort_by,
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if request.GET.get('buy_now') == '1':
        cart = {
            product_id: 1
            }
    elif product_id in cart:
        if cart[product_id] < product.stock:
            cart[product_id] += 1

    else:
        cart[product_id] = 1
        

    if request.GET.get('buy_now') == '1':
        return redirect('checkout')

    return redirect('cart')

def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        quantity = int(request.POST.get('quantity', 1))

        if quantity <= 0:
            del cart[product_id]
        elif quantity <= product.stock:
            cart[product_id] = quantity

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def cart(request):
    cart_data = request.session.get('cart', {})

    cart_items = []
    subtotal = 0

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=product_id)

        item_subtotal = product.price * quantity
        subtotal += item_subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': item_subtotal,
        })

    # Delivery charge
    if subtotal >= 499:
        delivery = 0
    else:
        delivery = 50

    total = subtotal + delivery
    if delivery == 0:
        free_delivery_message = ""
    else:
        free_delivery_message = 499 - subtotal

    

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery': delivery,
        'total': total,
        'free_delivery_message': free_delivery_message,
    })

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists.'
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_data = request.session.get('cart', {})

    if not cart_data:
        return redirect('cart')

    cart_items = []
    subtotal = 0

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=product_id)

        item_subtotal = product.price * quantity
        subtotal += item_subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': item_subtotal,
        })

    if subtotal >= 499:
        delivery = 0
    else:
        delivery = 50

    total = subtotal + delivery

    # Create order when form is submitted
    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            total_amount=total,
            payment_method=payment_method
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )

        # Clear cart after successful order
        request.session['cart'] = {}
        request.session.modified = True

        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery': delivery,
        'total': total,
    })

def order_confirmation(request, order_id):
    if not request.user.is_authenticated:
        return redirect('login')

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(request, 'order_confirmation.html', {
        'order': order
    })

def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('login')

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'product_detail.html', {
        'product': product,
    })

