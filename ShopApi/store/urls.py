from django.urls import path

from store.views import CategoryView, UpdateCategoryView, ProductView, UpdateProductView, CartView, UpdateCartView, \
    CartItemView, UpdateCartItemView, TransactionView, UpdateTransactionView, OrderView, UpdateOrderView, \
    DetailCategoryView, DetailProductView, DetailCartView, DetailCartItemView, DetailTransactionView, DetailOrderView, \
    DeleteCartItemView, DeleteOrderView, CategoryProductView, UpdateQuantityCartItem, CartProductView

urlpatterns = [
    #category
    path('categories',CategoryView.as_view()),
    path('category/create',CategoryView.as_view()),
    path('category/<int:pk>',DetailCategoryView.as_view()),
    path('category/update/<int:pk>',UpdateCategoryView.as_view()),


    #product
    path('products',ProductView.as_view()),
    path('product/create',ProductView.as_view()),
    path('product/<int:pk>',DetailProductView.as_view()),
    path('product/update/<int:pk>',UpdateProductView.as_view()),
    path('products/<str:category>',CategoryProductView.as_view()),


    #cart
    path('carts',CartView.as_view()),
    path('cart/create',CartView.as_view()),
    path('cart/<int:pk>',DetailCartView.as_view()),
    path('cart/update/<int:pk>',UpdateCartView.as_view()),


    #cartItem
    path('cartItems',CartItemView.as_view()),
    path('cartItem/create',CartItemView.as_view()),
    path('cartItem/<int:pk>',DetailCartItemView.as_view()),
    path('cartItem/update/<int:pk>',UpdateCartItemView.as_view()),
    path('cartItem/delete/<int:pk>',DeleteCartItemView.as_view()),
    path('cartItem/quantity/<int:pk>',UpdateQuantityCartItem.as_view()),
    path('cart/products/<int:pk>',CartProductView.as_view()),


    #transaction
    path('transactions',TransactionView.as_view()),
    path('transaction/create',TransactionView.as_view()),
    path('transaction/<int:pk>',DetailTransactionView.as_view()),
    path('transaction/update/<int:pk>',UpdateTransactionView.as_view()),


    #order
    path('orders',OrderView.as_view()),
    path('order/create',OrderView.as_view()),
    path('order/<int:pk>',DetailOrderView.as_view()),
    path('order/update/<int:pk>',UpdateOrderView.as_view()),
    path('order/delete/<int:pk>',DeleteOrderView.as_view()),




]