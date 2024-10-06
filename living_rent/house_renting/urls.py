from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('parcels/', views.parcel_list, name='parcel_list'),
    path('parcel/<int:pk>/', views.parcel_detail, name='parcel_detail'),
    path('cars_for_rent/', views.cars_for_rent, name='cars_for_rent'),
    path('cars_for_sale/', views.cars_for_sale, name='cars_for_sale'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('apartments/', views.apartment_list, name='apartment_list'),
    path('apartment/<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('offices/', views.office_list, name='office_list'),
    path('search/', views.search, name='search'), 
    path('notifications/', views.notifications, name='notifications'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)