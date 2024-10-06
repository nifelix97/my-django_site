from django.contrib import admin
from .models import Notification
from .models import Landlord, House, HouseImage, StudentApplication, Parcel, ParcelImage, ParcelApplication, Car, CarImage, CarApplication,Apartment

class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline]
class ParcelImageInline(admin.TabularInline):
    model = ParcelImage
    extra = 1
class ParcelAdmin(admin.ModelAdmin):
    inlines = [ParcelImageInline]

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('message',)

admin.site.register(Notification, NotificationAdmin)

admin.site.register(Landlord)
admin.site.register(House, HouseAdmin)
admin.site.register(StudentApplication)
admin.site.register(Parcel, ParcelAdmin)
admin.site.register(ParcelApplication)
admin.site.register(Car, CarAdmin)
admin.site.register(CarApplication)
admin.site.register(Apartment)

