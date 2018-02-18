from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Restaurant
		fields = ['name' , 'description', 'openingtime','closingtime']
		