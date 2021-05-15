from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categorie'

Label = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('D', 'Danger')
)

Size = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
)

class Product(models.Model):
    title = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    label = models.CharField(choices=Label, max_length=2, null=True, blank=True)
    size = models.CharField(choices=Size, max_length=2, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)

    def __str__(self):
        return str(self.category)

    @property
    def imageUrl(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url

    @property
    def imageUrl2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def imageUrl3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def imageUrl4(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url
        
class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product.category)

    @property
    def get_item_total(self):
        total = self.product.price * self.quantity
        return total

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_product = models.ManyToManyField(OrderProduct)
    order_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.customer.user.username

    @property
    def get_cart_total(self):
        orderProducts = self.order_product_set.all()
        total = sum([item.get_item_total for item in orderProducts])
        return total

    @property
    def get_cart_items_total(self):
        orderProducts = self.orderproduct_set.all()
        total = sum([item.quantity for item in orderProducts])
        return total

class SavedProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.user.username

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    confirmation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.username

    class Meta:
        verbose_name = 'Shipping Addres'

class Contact(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(default='admin@gmail.com')
    phone1 = models.CharField(max_length=200, null=True, blank=True)
    phone2 = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.address

class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.custormer.user.username
    
    
class Complaint(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.customer.user.username
    