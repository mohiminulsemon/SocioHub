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
        if commit == True:
            user.is_active = False
            user.save()
            UserDetails.objects.create(
                user=user,
                birth_date=self.cleaned_data['birth_date'],
                gender=self.cleaned_data['gender'],
                street_address=self.cleaned_data['street_address'],
                city=self.cleaned_data['city'],
                country=self.cleaned_data['country']
            )
        return user
    
    
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




class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        # Check if the user has UserDetails related to their account
        if self.instance and hasattr(self.instance, 'address'):
            user_address = self.instance.address
            self.fields['gender'].initial = user_address.gender
            self.fields['birth_date'].initial = user_address.birth_date
            self.fields['street_address'].initial = user_address.street_address
            self.fields['city'].initial = user_address.city
            self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            # Get or create UserDetails for the user
            user_address, created = UserDetails.objects.get_or_create(user=user)

            # Update UserDetails fields
            user_address.gender = self.cleaned_data['gender']
            user_address.birth_date = self.cleaned_data['birth_date']
            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user