from rest_framework import viewsets
from .models import Landlord, House, HouseImage, StudentApplication, Parcel, ParcelImage, ParcelApplication
from .serializers import LandlordSerializer, HouseSerializer, HouseImageSerializer, StudentApplicationSerializer, ParcelSerializer, ParcelImageSerializer, ParcelApplicationSerializer

class LandlordViewSet(viewsets.ModelViewSet):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseImageViewSet(viewsets.ModelViewSet):
    queryset = HouseImage.objects.all()
    serializer_class = HouseImageSerializer

class StudentApplicationViewSet(viewsets.ModelViewSet):
    queryset = StudentApplication.objects.all()
    serializer_class = StudentApplicationSerializer

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class ParcelImageViewSet(viewsets.ModelViewSet):
    queryset = ParcelImage.objects.all()
    serializer_class = ParcelImageSerializer

class ParcelApplicationViewSet(viewsets.ModelViewSet):
    queryset = ParcelApplication.objects.all()
    serializer_class = ParcelApplicationSerializer