from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('login')

    context = {'form': form}
    return render(request, 'store/register.html', context)


def login_request(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="store/login.html", context={"login_form": form,
                                                                      'categories': categories})
           

def logoutUser(request):
    logout(request)
    print("Log out test")
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


@login_required
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, createdOrder = Order.objects.get_or_create(customer=customer)
        kits = order.orderedproduct_set.all()
    else:
        kits = []
        order = {'get_total_from_cart':0, 'get_kit_from_cart':0}

    context = {'kits': kits, 'order':order}
    return render(request, 'store/cart.html', context)

@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, createdOrder = Order.objects.get_or_create(customer=customer,)
        kits = order.orderedproduct_set.all()
    else:
        kits = []
        order = {'get_total_from_cart':0, 'get_kit_from_cart':0}

    context = {'kits': kits, 'order':order}
    return render(request, 'store/checkout.html', context)
