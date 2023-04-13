from random import randint

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Payment
from .models import Category, Product, Cart, CartItem, Transaction, Order
from .Serializers.store_serializer import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, \
    TransactionSerializer, OrderSerializer


# Category
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategoryView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product
class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, category):
        categoryProduct = Product.objects.filter(category__name=category)
        serializer = ProductSerializer(categoryProduct, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Cart
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['cartSession'] = randint(1,10000000000000000)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)



class UpdateCartView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCartView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request, pk):
        cartProduct = CartItem.objects.filter(cart__person=pk)
        serializer = CartItemSerializer(cartProduct, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CartItem
class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            cart = serializer.validated_data['cart']
            cartItems = CartItem.objects.filter(cart=cart)

            product = serializer.validated_data['product']
            is_valid = True
            for cartItem in cartItems:
                if product == cartItem.product:
                    cartItem.quantity += serializer.validated_data['quantity']
                    cartItem.cost = cartItem.productPrice * cartItem.quantity
                    cartItem.save()
                    is_valid = False
                    return Response({'The Product is already in the cart and the quantity has been increase '})

            if is_valid:
                serializer.validated_data['productPrice'] = product.price
                quantity = serializer.validated_data['quantity']
                productPrice = serializer.validated_data['productPrice']
                serializer.validated_data['cost'] = quantity * productPrice
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Error creating Cart Item'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateCartItemView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class DetailCartItemView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class DeleteCartItemView(APIView):
    def delete(self, request, pk):
        cartItem = CartItem.objects.get(pk=pk)
        cartItem.delete()
        return Response({'delete': 'Item Removed Successfully'}, status=status.HTTP_204_NO_CONTENT)


class UpdateQuantityCartItem(APIView):
    def patch(self, request, pk):
        cartItem = CartItem.objects.get(pk=pk)
        serializer = CartItemSerializer(cartItem, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Error updating transaction'}, status=status.HTTP_400_BAD_REQUEST)


# Transaction
class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UpdateTransactionView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class DetailTransactionView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# check if the product is available
# check if the quantity is available and subtract the quantity (update the quantity)
# if the account balance is enough subtract the amount (update the balance)
# create the transaction
# create the order

# Order
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # I need to see the sample data
    def post(self, request):
        # You cannot be fetching 1000000 products
        products = Product.objects.all()
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Are you sure you have this data
            cart = serializer.validated_data['cart']
            cartItems = CartItem.objects.filter(cart=cart)

            cost = 0
            product_is_valid = False

            for cartItem in cartItems:

                if cartItem.product in products:
                    # what is the difference between cart Item and Item here
                    item = Product.objects.get(pk=cartItem.product.pk)
                    # what are you trying to explain here
                    if cartItem.quantity <= item.quantity:
                        cost = cost + cartItem.cost
                        item.quantity = item.quantity - cartItem.quantity
                        product_is_valid = True
                        item.save()

                    # else:
                    #     cartItem.quantity = item.quantity
                    #     cartItem.cost = cartItem.productPrice * item.quantity
                    #     cost = cost + cartItem.cost
                    #     cartItem.save()
                    #     item.quantity = item.quantity - cartItem.quantity
                    #     product_is_valid = True
                    #     item.save()
                # why are you deleting here
                else:
                    cartItem.delete()

            if product_is_valid:

                payment = Payment.objects.get(person=cart.person)

                if cost <= payment.balance:
                    payment.balance -= cost
                    payment.save()
                    transaction = Transaction(
                        ref=payment.cardNumber,
                        amount=cost,
                        person=cart.person,
                        paymentMethod=payment,
                        status=serializer.validated_data['status'],
                        cart=cart,
                    )

                    transaction.save()
                    # why are you passing this value into the serializer
                serializer.validated_data['transaction'] = transaction
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'Error': 'Order not Created'})


class UpdateOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeleteOrderView(APIView):
    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'delete': 'Order Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)


class DetailOrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# check if the product is available
# check if the quantity is available and subtract the quantity (update the quantity)
# if the account balance is enough subtract the amount (update the balance)
# create the transaction
# create the order

#
# class CreateOrder(APIView):
#     def post(self,request):
#         product =Product.objects.all()
#         order = Order.objects.all()
#         serializer = OrderSerializer(order,data=request.data)
#         if serializer.is_valid():
#             if serializer.validated_data['product'] == product:
#                 return Response({'confirmed':'The product is available'})
#             return Response({'confirmed': 'The product is not available'})
#             serializer.save()
#         return Response({'confirmed': 'Order Created'})




# payment = serializer.validated_data['payment']
                # balance = payment.balance
                # order_payment = Payment.objects.get(pk=payment.pk)

                # if cost <= balance:
                #     order_payment.balance = order_payment.balance - cost
                #     order_payment.save()

