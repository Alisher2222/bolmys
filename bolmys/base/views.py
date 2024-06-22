from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import TripForm
from .models import Trip,UserTrip
from django.contrib.auth.decorators import login_required
from user.forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from user.models import CustomUser

User = get_user_model()

def home(request):
    return render(request, 'base/home.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'base/login.html')

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("home")

def registerUser(request):
    userForm = CustomUserCreationForm()
    if request.method == "POST":
        userForm = CustomUserCreationForm(request.POST, request.FILES) 
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.lower()
            user.save()
            auth_login(request, user)
            group = Group.objects.get(name='user')
            user.groups.add(group)
            return redirect('home')
        else:
            messages.error(request, "Registration error")
    return render(request, "base/register.html", {'userForm': userForm})

@login_required(login_url="login")
def addTrip(request):
    error = ""
    tripForm = TripForm()
    if request.method == "POST":
        tripForm = TripForm(request.POST)
        if tripForm.is_valid():
            trip = tripForm.save(commit=False)
            trip.user_created_id = request.user.id
            trip.save()
            return redirect("home")
        else:
            error = "Please correct the following errors:"
            for field, errors in tripForm.errors.items():
                error += f"\n{field}: {', '.join(errors)}"
    return render(request, 'base/addTrip.html', {'tripForm': tripForm, 'error': error})
@login_required(login_url="login")
def viewTrips(request):
    trips = Trip.objects.filter(user_created=request.user)
    return render(request, 'base/viewTrips.html', {'trips':trips})
@login_required(login_url="login")
@login_required(login_url="login")
def trips(request):
    trips = Trip.objects.all()

    # Получение уникальных значений origin и destination для отображения в фильтрах
    origins = Trip.objects.values_list('origin', flat=True).distinct()
    destinations = Trip.objects.values_list('destination', flat=True).distinct()

    # Фильтр по origin и destination
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    if origin:
        trips = trips.filter(origin__icontains=origin)
    if destination:
        trips = trips.filter(destination__icontains=destination)

    # Поиск по названию места назначения
    searchedDestinition = request.GET.get('searchedDestinition')
    if searchedDestinition:
        trips = trips.filter(destination__icontains=searchedDestinition)

    return render(request, 'base/trips.html', {'trips': trips, 'origins': origins, 'destinations': destinations})

@login_required(login_url="login")
def trip(request, id):
    if request.method == "POST":
        trip = Trip.objects.get(id=id)
        if UserTrip.objects.filter(user=request.user, trip=trip).exists():
            messages.error(request, "The user has already left their contact details.")
        else:
            user_trip = UserTrip(
                user=request.user,
                trip=trip,
                name = trip.name
            )
            user_trip.save()
            messages.success(request, "Contact details submitted successfully!")
        
        return redirect('trip', id=id)  # include the id parameter
    
    trip = Trip.objects.get(id=id)
    return render(request, 'base/trip.html', {'trip': trip})

@login_required(login_url="login")
def usersContact(request, id):
    trip = Trip.objects.get(id=id)
    user_trips = UserTrip.objects.filter(trip=trip)
    users = [user_trip.user for user_trip in user_trips]  # Extract User objects
    return render(request, 'base/usersContact.html', {'users': users})

@login_required(login_url="login")
def userProfile(request,id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'base/userProfile.html',{'user':user})
@login_required(login_url="login")
def userChange(request, id):
    user = CustomUser.objects.get(id=id)
    userForm = CustomUserUpdateForm(instance=user)
    if request.method == "POST":
        userForm = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if userForm.is_valid():
            userForm.save()
            return redirect('home')
    return render(request, 'base/userChange.html', {'userForm': userForm})

