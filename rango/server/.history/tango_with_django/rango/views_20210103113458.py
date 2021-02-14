from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rango.forms import CategoryForm, PageForm
from django.urls import reverse
from .models import Category, Page, User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    categories = Category.objects.order_by('-likes')[:4]
    pages = Page.objects.order_by('-views')[:5]
    context = {'cat': categories, 'pages': pages}
    return render(request, 'rango/index.html', context)


def category(request, category_name):
    category = Category.objects.get(name=category_name)
    pages = Page.objects.filter(category=category)
    context = {'category': category, 'pages': pages}
    return render(request, 'rango/category.html', context)


def page(request, page_name):
    page = Page.objects.get(title=page_name)
    context = {'page': page}
    return render(request, 'rango/page.html', context)


def add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect(reverse('rango:index'))
        else:
            return render(request, 'rango/add_category.html', {'form': form})
    else:
        form = CategoryForm()
        return render(request, 'rango/add_category.html', {'form': form})


def addpage(request, cat_name):
    category = Category.objects.get(name=cat_name)
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        url = 'https://' + url
        Page.objects.create(category=category, title=title, url=url)
        return HttpResponseRedirect(reverse('rango:category', args=(category.name,)))
    else:
        return render(request, 'rango/add_page.html', {'cat': category})


def about(request):
    return HttpResponse("I'm cool")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # url = request.POST['url']
        # profile_pic = request.POST['profile_pic']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password == confirmation:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return HttpResponseRedirect(reverse('rango:login'))
            except IntegrityError:
                return render(request, 'rango/register.html', {'integrityerror': 'Sorry, username already exist.'})
        else:
            return render(request, 'rango/register.html', {'passworderror': "Password doesn't match."})
    else:
        return render(request, 'rango/register.html')
  

# def login(request):
#     return render(request, 'rango/login.html', {})


def log(request):
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('rango:index'))
        else:
            return render(request, 'rango/login.html', {'loginerror': "Invalid username and/or password."})
    else:
        return render(request, 'rango/login.html')
