from django.shortcuts import render, redirect
from .models import Restaurant, Item
from .forms import RestaurantForm, RegisterUserModel, LoginForm, ItemForm
from django.contrib.auth import authenticate, login ,logout

def list(request):
    my_restaurants_list={
    'restaurants': Restaurant.objects.all(),
    # [
    #   {
    #   'name':'Rehams Restaurant',
    #   'description':'This is my restaurant!',
    #   'openingtime':'09:00AM',
    #   'closingtime':'10:00PM',
    #   },
    #   {
    #   'name':'Rainy Days',
    #   'description':'Yummyyy!',
    #   'openingtime':'09:00AM',
    #   'closingtime':'10:00PM',
    #   },
    #   {
    #   'name':'The Strong Ones',
    #   'description':'For Body Builders!',
    #   'openingtime':'09:00AM',
    #   'closingtime':'10:00PM',
    #   },
    #   {
    #   'name':'Vegans',
    #   'description':'For Vegans!',
    #   'openingtime':'09:00AM',
    #   'closingtime':'10:00PM',
    #   },
    # ]
    }
    return render(request,'list.html',my_restaurants_list)

def detail(request, my_id):
    restaurant = Restaurant.objects.get(id=my_id)
    items = Item.objects.filter(restaurant=restaurant)
    context={
        'restaurant': restaurant,
        'items' : items,
    }
    return render(request,'detail.html',context)

def form(request):
    my_form = RestaurantForm()
    if request.method == 'POST':
        my_form = RestaurantForm(request.POST, request.FILES or None)
        if my_form.is_valid():
            my_form.save()
            return redirect('list')
    context={
        'my_form': my_form,
    }
    return render(request,'my_form.html',context)

def create_item(request,res_id):
    my_item = ItemForm()
    resobj = Restaurant.objects.get(id=res_id)
    if request.method == 'POST':
        my_item = ItemForm(request.POST)
        if my_item.is_valid():
            my_item = my_item.save(commit=False)
            my_item.restaurant = resobj
            my_item.save()
            return redirect('detail',my_id=resobj.id)
    context={
        'my_item': my_item,
        'resobj' : resobj,
    }
    return render(request,'create_item.html',context)

def update(request, res_id):
    resobj = Restaurant.objects.get(id=res_id)
    my_form = RestaurantForm(instance=resobj)
    if request.method == 'POST':
        my_form = RestaurantForm(request.POST, request.FILES or None, instance=resobj)
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

def register(request):
    my_form = RegisterUserModel()
    if request.method == 'POST':
        my_form = RegisterUserModel(request.POST)
        if my_form.is_valid():
            person = my_form.save(commit=False)
            person.set_password(person.password)
            person.save()
            username = my_form.cleaned_data['username']
            password = my_form.cleaned_data['password']
            authen = authenticate(username=username,password=password)
            if authen is not None:
                login(request, authen)
                return redirect('list')
    context={
        'my_form': my_form,
    }
    return render(request,'register.html',context)

def user_login(request):
    my_form = LoginForm()
    if request.method == 'POST':
        my_form = LoginForm(request.POST)
        if my_form.is_valid():
            username = my_form.cleaned_data['username']
            password = my_form.cleaned_data['password']
            authen = authenticate(username=username,password=password)
            if authen is not None:
                login(request, authen)
                return redirect('list')
    context={
        'my_form': my_form,
    }
    return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('login')
