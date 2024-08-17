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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)