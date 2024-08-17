from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import LandlordViewSet, HouseViewSet, HouseImageViewSet, StudentApplicationViewSet, ParcelViewSet, ParcelImageViewSet, ParcelApplicationViewSet

router = DefaultRouter()
router.register(r'landlords', LandlordViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'house-images', HouseImageViewSet)
router.register(r'student-applications', StudentApplicationViewSet)
router.register(r'parcels', ParcelViewSet)
router.register(r'parcel-images', ParcelImageViewSet)
router.register(r'parcel-applications', ParcelApplicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]