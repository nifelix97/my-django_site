from django.contrib import admin
from .models import Landlord, House, HouseImage, StudentApplication, Parcel, ParcelImage, ParcelApplication

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

admin.site.register(Landlord)
admin.site.register(House, HouseAdmin)
admin.site.register(StudentApplication)
admin.site.register(Parcel, ParcelAdmin)
admin.site.register(ParcelApplication)

