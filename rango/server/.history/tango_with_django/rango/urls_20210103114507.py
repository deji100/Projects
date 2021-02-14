from django.urls import path
from . import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('page/<str:page_name>/', views.page, name='page'),
    path('add/', views.add, name='add'),
    path('addpage/<str:cat_name>/', views.addpage, name='addpage'),
    path('register/', views.register, name='register'),
]
