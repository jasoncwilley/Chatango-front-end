from locator.models import Location
from django import forms


class LocatorForm(forms.ModelForm):
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Current City Name ','class': 'messageText', 'size':'25'}))
    longitude = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder': 'Longitude Coordinate','class': 'messageText', 'size':'16'}))
    latitude = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder': 'Latitude Coordinate','class': 'messageText', 'size':'16'}))

    class Meta:
        model = Location
        fields = ('city', 'longitude', 'latitude')
