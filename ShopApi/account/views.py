from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from account.Serializers.account_serializer import PersonSerializer, AddressSerializer, PaymentSerializer
from account.models import Person, Address, Payment


# Create your views here.

# class CreateUser(APIView):
#     def post(self, request,format=None):
#         print(request.body)
#         serializer = PersonSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
#             serializer.validated_data['is_active'] = True
#             serializer.save()
#             return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({'error': 'Error creating User'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self,format=None):
#         username = [user.username for user in Person.objects.all()]
#         return Response({'username':username}, status=status.HTTP_200_OK)


# def list(self, request, *args, **kwargs):
#     serializer = AddressSerializer(Address.objects.all(), many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

class CreateUser(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class UpdatePersonView(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class DetailAddressView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UpdateAddressView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class UpdatePaymentView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class AddressViewUser(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def list(self, request, *args, **kwargs):
        user = self.request.query_params.get('user')
        userAddress = Address.objects.filter(person=user)
        serializer = AddressSerializer(userAddress, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
