from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, TuitionProfile

#create your forms here
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        # fields = "__all__"
        exclude = ('user',)

class TuitionProfileForm(forms.ModelForm):
    class Meta:
        model = TuitionProfile
        # fields = "__all__"
        exclude = ('user',)
        widgets = {
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
        }
