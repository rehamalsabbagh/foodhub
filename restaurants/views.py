from django.shortcuts import render
from .models import Restaurant

def list(request):
	my_restaurants_list={
	'restaurants': Restaurant.objects.all(),
	# [
	# 	{
	# 	'name':'Rehams Restaurant',
	# 	'description':'This is my restaurant!',
	# 	'openingtime':'09:00AM',
	# 	'closingtime':'10:00PM',
	# 	},
	# 	{
	# 	'name':'Rainy Days',
	# 	'description':'Yummyyy!',
	# 	'openingtime':'09:00AM',
	# 	'closingtime':'10:00PM',
	# 	},
	# 	{
	# 	'name':'The Strong Ones',
	# 	'description':'For Body Builders!',
	# 	'openingtime':'09:00AM',
	# 	'closingtime':'10:00PM',
	# 	},
	# 	{
	# 	'name':'Vegans',
	# 	'description':'For Vegans!',
	# 	'openingtime':'09:00AM',
	# 	'closingtime':'10:00PM',
	# 	},
	# ]
	}
	return render(request,'list.html',my_restaurants_list)

def detail(request, my_id):
	context={
		'restaurant': Restaurant.objects.get(id=my_id),
		# 'name':'Rehams Restaurant',
		# 'description':'This is my restaurant!',
		# 'openingtime':'09:00AM',
		# 'closingtime':'10:00PM',
	}
	return render(request,'html-file.html',context)


# Create your views here.
