from django.contrib import admin
from .models import Category,Product,Cart,CartItem,Transaction,Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Transaction)
admin.site.register(Order)

# Register your models here.
