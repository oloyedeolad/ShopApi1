from django.urls import path

from account.views import CreateUser, AddressView, DetailAddressView, UpdateAddressView, PaymentView, UpdatePaymentView, \
    UpdatePersonView,AddressViewUser

urlpatterns = [
    path('user',CreateUser.as_view()),
    path('user/create',CreateUser.as_view()),
    path('user/update/<int:pk>',UpdatePersonView.as_view()),

    path('address/<int:user>',AddressViewUser.as_view()),
    path('address/create',AddressView.as_view()),
    path('address/<int:pk>',DetailAddressView.as_view()),
    path('address/update/<int:pk>',UpdateAddressView.as_view()),

    path('payment',PaymentView.as_view()),
    path('payment/create',PaymentView.as_view()),
    path('payment/update/<int:pk>',UpdatePaymentView.as_view())
]