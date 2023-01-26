from django import forms
from customer.models import Customer
from core.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']
        widgets={
            'first_name': forms.TextInput(attrs={'required':True, 'placeholder':"Enter First Name", 'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'required': True, 'placeholder':"Enter Last Name", 'class': "form-control"}),
            }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'password']
        widgets={
            'phone': forms.TextInput(attrs={'required': True, 'placeholder':"Enter Your Phone", 'class':"form-control"}),
            'password': forms.TextInput(attrs={'placeholder':"Enter Your Password", 'class': "form-control"}),
            }