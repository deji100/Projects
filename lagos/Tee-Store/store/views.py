from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .forms import *
from .models import *


# Create your views here.

def index(request):
    pass


# @login_required(login_url='login')
def store(request):
    page = request.GET.get('page', 1)

    product_list = Product.objects.all()
    paginator = Paginator(product_list, 8)

    category = Category.objects.all()

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'store.html', {'products': products, 'category': category})


def get_product_by_category(request, category):
    page = request.GET.get('page', 1)

    product_list = Product.objects.filter(category=category)
    paginator = Paginator(product_list, 8)

    category = Category.objects.all()

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'products': products, 'category': category})


def product(request, id):
    product = Product.objects.get(id=id)
    comments = product.comment_set.order_by('-time')[:15]
    return render(request, 'product.html', {'product': product, 'comments': comments})


def display_saved_products(request):
    if 'product' in request.session:
        request.session = []
    return render(request, 'saved.html', {'product': request.session})


def add_saved_product(request, id):
    if not 'product' in request.session:
        product = Product.objects.get(id=id)
        request.session = [product]
        return redirect('saved_product')


def delete_saved_product(request, id):
    if 'product' in request.session:
        product = Product.objects.get(id=id)
        del request.session[product]
        return redirect('saved_product')


def process_comment(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            customer, create = Customer.objects.get_or_create(user=user)

        comment = request.POST.get('comment')
        product = Product.objects.get(id=id)
        save_comment = Comment.objects.create(customer=customer, product=product, comment=comment, time=timezone.now())
        return HttpResponseRedirect(reverse('product', args=(product.id,)))
    


@login_required(login_url='login')
def cart(request):
    pass

@login_required(login_url='login')
def checkout(request):
    pass

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Fill in correct credentials.'})
    
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('login')

    form = CreateUserForm()
    return render(request, 'register.html', {'form': form})