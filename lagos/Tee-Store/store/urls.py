from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('products/<int:category>/', views.get_product_by_category, name='products'),
    path('product/<int:id>/', views.product, name='product'),
    path('comment/<int:id>/', views.process_comment, name='comment'),
    path('saved_products', views.display_saved_products, name='saved_product'),
    path('save/<int:id>/', views.add_saved_product, name='add_product'),
    path('delete/<int:id>', views.delete_saved_product, name='delete_saved_product'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register')
]

