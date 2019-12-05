from django import forms

from django.contrib.auth.models import User
from foodtaskerapp.models import Restaurant, Meal

 
# Forms used to authenticate Users
class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")


# Forms used for Restaurant administrator to edit their own details
class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


# Form used for signing up a new restaurant
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "phone", "address", "logo")


# Form used to add a new meal
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ("restaurant", )
