from django.forms import ModelForm
from .models import Trip, UserTrip

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = [
            'name','company','origin','destination','description','price','duration','transport_type'
        ]
class UserTripForm(ModelForm):
    class Meta:
        model = UserTrip
        fields = [
            'user','trip','name'
        ]
