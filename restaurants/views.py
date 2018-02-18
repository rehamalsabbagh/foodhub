from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

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

def form(request):
	my_form = RestaurantForm()
	if request.method == 'POST':
		my_form = RestaurantForm(request.POST)
		if my_form.is_valid():
			my_form.save()
	context={
		'my_form': my_form,
	}
	return render(request,'my_form.html',context)

def update(request, res_id):
	resobj = Restaurant.objects.get(id=res_id)
	my_form = RestaurantForm(instance=resobj)
	if request.method == 'POST':
		my_form = RestaurantForm(request.POST, instance=resobj)
		if my_form.is_valid():
			my_form.save()
			return redirect('detail',my_id=resobj.id)
	context={
		'my_form': my_form,
		'resobj' :resobj,
	}
	return render(request,'update_form.html',context)

def delete(request,res_id):
	Restaurant.objects.get(id=res_id).delete()
	return redirect('list')
