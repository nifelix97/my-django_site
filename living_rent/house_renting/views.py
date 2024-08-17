from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import House, StudentApplication,Parcel
from .forms import StudentApplicationForm,ParcelApplicationForm,ParcelApplication


def home(request):
    houses = House.objects.filter(available=True)
    return render(request, 'house_renting/home.html', {'houses': houses})

@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    houses = House.objects.all()
    available_houses_count = houses.filter(available=True).count()
    house_types = houses.values_list('house_type', flat=True).distinct()
    parcels = Parcel.objects.all()
    parcel_count = parcels.count()  # Define parcel_count variable
    return render(request, 'house_renting/dashboard.html', {
        'houses': houses,
        'available_houses_count': available_houses_count,
        'house_types': house_types,
        'parcels': parcels,
        'parcel_count': parcel_count,
    })

def parcel_list(request):
    parcels = Parcel.objects.all()
    parcel_count = parcels.count()  # Count the number of parcels
    return render(request, 'house_renting/parcel_list.html', {
        'parcels': parcels,
        'parcel_count': parcel_count  # Pass the count to the template
    })
def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    images = house.images.all()  # Get all related images
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.house = house
            application.save()
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
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('parcel_detail', pk=pk)
    else:
        form = ParcelApplicationForm()
    return render(request, 'house_renting/parcel_detail.html', {
        'parcel': parcel,
        'images': images,
        'form': form
    })
