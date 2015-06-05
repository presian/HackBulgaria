from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ['username', 'row', 'col']
