from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from .models import House, StudentApplication, Parcel, Car, CarApplication, Apartment, Notification
from .forms import StudentApplicationForm, ParcelApplicationForm, ParcelApplication, CarApplicationForm, ApartmentForm

def property_list(request):
    cars_for_rent = Car.objects.filter(rent__gt=0)
    cars_for_sale = Car.objects.filter(sale_price__gt=0)
    apartments = Apartment.objects.all()
    parcels = Parcel.objects.all()
    offices = Apartment.objects.filter(type='OFFICE')
    houses = House.objects.all()  # Fetch houses

    context = {
        'cars_for_rent': cars_for_rent,
        'cars_for_sale': cars_for_sale,
        'apartments': apartments,
        'parcels': parcels,
        'offices': offices,
        'houses': houses,  # Add houses to context
    }
    return render(request, 'house_renting/property_list.html', context)

def create_notification(message):
    Notification.objects.create(message=message)

def notifications(request):
    notifications = Notification.objects.all().order_by('-created_at')
    Notification.objects.filter(is_read=False).update(is_read=True)
    return render(request, 'house_renting/notifications.html', {'notifications': notifications})

def search(request):
    query = request.GET.get('q')
    if query:
        houses = House.objects.filter(Q(address__icontains=query) | Q(description__icontains=query))
        apartments = Apartment.objects.filter(Q(address__icontains=query) | Q(description__icontains=query))
        offices = Apartment.objects.filter(type='OFFICE').filter(Q(address__icontains=query) | Q(description__icontains=query))
        parcels = Parcel.objects.filter(Q(address__icontains=query) | Q(description__icontains=query))
        cars = Car.objects.filter(Q(car_name__icontains=query) | Q(description__icontains=query))
    else:
        houses = apartments = offices = parcels = cars = []

    context = {
        'houses': houses,
        'apartments': apartments,
        'offices': offices,
        'parcels': parcels,
        'cars': cars,
        'query': query,
    }
    return render(request, 'house_renting/search_results.html', context)

def home(request):
    houses = House.objects.filter(available=True)
    return render(request, 'house_renting/home.html', {'houses': houses})

@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    houses = House.objects.all()
    available_houses_count = houses.filter(available=True).count()
    house_types = houses.values_list('house_type', flat=True).distinct()
    parcels = Parcel.objects.all()
    parcel_count = parcels.count()
    cars = Car.objects.all()
    car_count = cars.count()
    return render(request, 'house_renting/dashboard.html', {
        'houses': houses,
        'available_houses_count': available_houses_count,
        'house_types': house_types,
        'parcels': parcels,
        'parcel_count': parcel_count,
        'cars': cars,
        'car_count': car_count
    })

def parcel_list(request):
    parcels = Parcel.objects.all()
    parcel_count = parcels.count()
    return render(request, 'house_renting/parcel_list.html', {
        'parcels': parcels,
        'parcel_count': parcel_count
    })

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    images = house.images.all()
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.house = house
            application.save()
            create_notification(f"New application for house: {house.address}")
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('house_detail', pk=pk)
    else:
        form = StudentApplicationForm()
    return render(request, 'house_renting/house_detail.html', {
        'house': house,
        'images': images,
        'form': form
    })

def contact(request):
    return render(request, 'house_renting/contact.html')

def parcel_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'house_renting/parcel_list.html', {'parcels': parcels})

def parcel_detail(request, pk):
    parcel = get_object_or_404(Parcel, pk=pk)
    images = parcel.images.all()
    if request.method == 'POST':
        form = ParcelApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.parcel = parcel
            application.save()
            create_notification(f"New application for parcel: {parcel.address}")
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('parcel_detail', pk=pk)
    else:
        form = ParcelApplicationForm()
    return render(request, 'house_renting/parcel_detail.html', {
        'parcel': parcel,
        'images': images,
        'form': form
    })

def cars_for_rent(request):
    cars = Car.objects.filter(rent__gt=0)
    return render(request, 'house_renting/cars_for_rent.html', {
        'cars': cars
    })

def cars_for_sale(request):
    cars = Car.objects.filter(sale_price__gt=0)
    return render(request, 'house_renting/cars_for_sale.html', {
        'cars': cars
    })

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    images = car.images.all()
    if request.method == 'POST':
        form = CarApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.car = car
            application.save()
            create_notification(f"New application for car: {car.car_name}")
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('car_detail', pk=pk)
    else:
        form = CarApplicationForm()
    return render(request, 'house_renting/car_detail.html', {
        'car': car,
        'images': images,
        'form': form
    })

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'house_renting/apartment_list.html', {'apartments': apartments})

def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment details updated successfully!')
            return redirect('apartment_detail', pk=pk)
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'house_renting/apartment_detail.html', {
        'apartment': apartment,
        'form': form
    })

def office_list(request):
    offices = Apartment.objects.filter(type='OFFICE')
    return render(request, 'house_renting/office_list.html', {'offices': offices})