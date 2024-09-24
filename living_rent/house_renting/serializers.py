from rest_framework import serializers
from .models import Landlord, House, HouseImage, StudentApplication, Parcel, ParcelImage, ParcelApplication, Car, CarImage, CarApplication

class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = '__all__'

class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplication
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class ParcelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelImage
        fields = '__all__'

class ParcelApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelApplication
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'

class CarApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplication
        fields = '__all__'