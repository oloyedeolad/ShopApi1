from django.db import models
from account.models import Person, Address, Payment


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    imageUrl = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cartSession = models.CharField(max_length=200,null=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


    def __str__(self):
        return str(self.person)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f'{str(self.cart)} - {str(self.product)} '



class Transaction(models.Model):
    ref = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    paymentMethod = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.person)



class Order(models.Model):
    shippingAddress = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name="shipping_address")
    billingAddress = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name="billing_address")
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=200)

    def __str__(self):
        return str(self.cart)
