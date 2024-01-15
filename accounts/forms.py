from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .constants import GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserDetails

class RegisterForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        user.is_active = False
        user_details = UserDetails.objects.create(
            user=user,
            birth_date=self.cleaned_data['birth_date'],
            gender=self.cleaned_data['gender'],
            street_address=self.cleaned_data['street_address'],
            city=self.cleaned_data['city'],
            country=self.cleaned_data['country']
        )

        if commit:
            user_details.save()

        return user, user_details
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
