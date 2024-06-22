from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('addTrip/', views.addTrip, name="addTrip"),
    path('viewTrips/', views.viewTrips, name="viewTrips"),
    path('trips/', views.trips, name="trips"),
    path('trip/<int:id>', views.trip, name="trip"),
    path('usersContact/<int:id>', views.usersContact, name="usersContact"),
    path('userProfile/<int:id>', views.userProfile, name = "userProfile"),
    path('userChange/<int:id>', views.userChange, name = "userChange"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
