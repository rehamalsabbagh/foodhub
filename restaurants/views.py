from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Restaurant, Item, FavourateRestaurant
from .forms import RestaurantForm, RegisterUserModel, LoginForm, ItemForm
from django.contrib.auth import authenticate, login ,logout

def list(request):
    if (request.user.is_anonymous):
        return redirect('login')
        
    my_restaurants_list = Restaurant.objects.all()

    query = request.GET.get("q")
    if query:
        my_restaurants_list = my_restaurants_list.filter(name__contains=query)

    context={
    'restaurants': my_restaurants_list,
    }
    return render(request,'list.html',context)

def detail(request, my_id):
    restaurant = Restaurant.objects.get(id=my_id)
    items = Item.objects.filter(restaurant=restaurant)
    fav_items = []
    favs = request.user.favouraterestaurant_set.all()
    for fav in favs:
        fav_items.append(fav.restaurant)
    context={
        'restaurant': restaurant,
        'items' : items,
        'fav_items' : fav_items,
    }
    return render(request,'detail.html',context)

def form(request):
    if (request.user.is_anonymous):
        return redirect('login')
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
    if not(request.user==resobj.owner or request.user.is_staff):
        return redirect('login')
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
    restaurant = Restaurant.objects.get(id=res_id)
    if (not(request.user.is_staff) or request.user==restaurant.owner):
        return redirect('login')
    restaurant.delete()
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

def favourate_res(request,res_id):
    resobj = Restaurant.objects.get(id=res_id)
    favobj , created = FavourateRestaurant.objects.get_or_create(user=request.user, restaurant=resobj)
    if created:
        action = 'fav'
    else:
        action = 'notfav'
        favobj.delete()
    fav_num = resobj.favouraterestaurant_set.all().count()


    # favobj = Like.objects.get(user=request.user, restaurant=resobj)
    # if favobj is None:
    #     favobj = Like.objects.create(user=request.user, restaurant=resobj)
    #     created = True
    # else:
    #     created = False

    context = {
        'action' : action,
        'fav_num' : fav_num,
    }

    return JsonResponse(context, safe=False)
