from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_list(request):
    # Only show approved products
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/delete_product.html', {'product': product})


def home(request):
    return render(request, 'home.html')

def aleppy(request):
    return render(request, 'aleppy.html')

def cochin(request):
    return render(request, 'cochin.html')

def munnar(request):
    return render(request, 'munnar.html')

def wayanad(request):
    return render(request, 'wayanad.html')




def packages(request):
    products = Product.objects.filter(is_approved=True)
    return render(request, 'packages.html',{'products': products})



# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('index')
    return render(request, 'logout.html')


def index(request):
    return render(request, 'index.html')




def vensg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('venlo')
    else:
        form = UserCreationForm()
    return render(request, 'vensg.html', {'form': form})

# Login view
def venlo(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'venlo.html', {'form': form})

# Logout view
def venlt(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('index')
    return render(request, 'venlt.html')


def base(request):
    return render(request, 'base.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list or a specific page
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        fform = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list or a specific page
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})



# views.py



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})






# views.py
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product

def create_order(request, product_id):
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    
    # Get product details
    product = Product.objects.get(id=product_id)
    
    # Create an order with Razorpay
    amount = int(product.price * 100)  # Amount in paise
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1',
        'receipt': f'order_{product_id}'
    }
    
    try:
        order = client.order.create(data=order_data)
        context = {
            'order_id': order['id'],
            'amount': amount,
            'currency': 'INR',
            'product_name': product.name
        }
        return render(request, 'payment.html', context)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)






# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        
        # Validate the payment (Optional: you may want to verify the payment signature)
        
        return render(request, 'payment_success.html')
    return JsonResponse({'error': 'Invalid request'}, status=400)

