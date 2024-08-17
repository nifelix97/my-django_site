from django.db import models
from django.db import models
from django.utils import timezone


class Landlord(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class House(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    house_type = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    rent = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    date_added = models.DateField(auto_now_add=True)  # Remove default here
    description = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='houses/main/')

    def __str__(self):
        return self.address
class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='houses/')

    def __str__(self):
        return f"{self.house.address} - Image"

class StudentApplication(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_contact_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f'{self.user_name} - {self.house.address}'
    
class Parcel(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='parcels/main/')

    def __str__(self):
        return self.address

class ParcelImage(models.Model):
    parcel = models.ForeignKey(Parcel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='parcels/')

    def __str__(self):
        return f"{self.parcel.address} - Image"

class ParcelApplication(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_contact_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f'{self.user_name} - {self.parcel.address}'
