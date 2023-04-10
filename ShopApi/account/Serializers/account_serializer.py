from rest_framework import serializers
from account.models import Person,Address,Payment

# short way of creating the serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','username','password','first_name','last_name','email','is_active','is_staff']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'



# Long way of creating the serializer
# class PersonSerializer(serializers.Serializer):
#     is_verified = serializers.BooleanField(default=False)

#
# class AddressSerializer(serializers.Serializer):
#     description = serializers.CharField(max_length=500)
#     country = serializers.CharField(max_length=100)
#     state = serializers.CharField(max_length=200)
#     addressType = serializers.CharField(max_length=200)
#
#
# class PaymentSerializer(serializers.Serializer):
#     cardNumber = serializers.CharField(max_length=20)
#     cardPin = serializers.IntegerField(max_length=4)
#     expiryDate = serializers.DateField()
#     cardCode = serializers.IntegerField()

