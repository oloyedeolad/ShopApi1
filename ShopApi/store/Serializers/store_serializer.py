from rest_framework import serializers
from store.models import Category,Product,Cart,CartItem,Transaction,Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        # fields = ['id','cart','product','quantity','productPrice']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



# Long Way to do the Serializers
# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=500)
#
#
# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=500)
#     price = serializers.DecimalField()
#     imageUrl = serializers.URLField()
#
#
# class CartSerializer(serializers.Serializer):
#     cartSession = serializers.CharField(max_length=200)
#
#
# class CartItemSerializer(serializers.Serializer):
#     quantity = serializers.IntegerField()
#     cost = serializers.DecimalField()
#     productPrice = serializers.DecimalField()
#
#
# class TransactionSerializer(serializers.Serializer):
#     ref = serializers.CharField(max_length=200)
#     amount = serializers.DecimalField()
#     paymentMethod = serializers.CharField(max_length=200)
#     status = serializers.CharField(max_length=200)
#
#
# class OrderSerializer(serializers.Serializer):
#     status = serializers.CharField(max_length=200)