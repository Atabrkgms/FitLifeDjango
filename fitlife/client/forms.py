from django import forms
from .models import Client

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_first_name', 'client_last_name', 'client_birthdate', 'client_gender', 'client_email', 'password', 'client_phone_number']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=Client.GENDER_CHOICES),
            'password': forms.PasswordInput(),
        }