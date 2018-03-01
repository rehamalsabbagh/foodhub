from django import forms
from .models import Restaurant ,Item
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Restaurant
		fields = ['name' , 'description', 'openingtime','closingtime','logo']
		widgets = {
			'openingtime': forms.TimeInput(attrs={'type':'time'}),
			'closingtime': forms.TimeInput(attrs={'type':'time'}),
		}
		
class RegisterUserModel(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = User
		fields = ['username' , 'email', 'first_name','last_name','password']
		widgets = {
			'password': forms.PasswordInput(),
		}

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True , widget=forms.PasswordInput())


class ItemForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Item
		fields = ['name' , 'description', 'price']
		# widgets = {
		# 	'openingtime': forms.TimeInput(attrs={'type':'time'}),
		# 	'closingtime': forms.TimeInput(attrs={'type':'time'}),
		# }