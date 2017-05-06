from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Restaurant
from .forms import RestForm

def rest_index(request):
    restaurant = Restaurant.objects.order_by('?').first()
    return render(request, 'app/rest_index.html',{
        'restaurant':restaurant
    })


@login_required
def rest_new(request):
    if request.method == 'POST':
        form = RestForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.author = request.user
            restaurant.save()
            messages.success(request, '식당이 랜덤리스트에 들어갔습니다.')
            #메세지 프레임워크
            return redirect(restaurant)
    else:
        form = RestForm()
    return render(request, 'app/rest_new.html',{
        'form': form
    })

@login_required
def rest_edit(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        form = RestForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.author = request.user
            restaurant.save()
            messages.success(request, '식당 정보를 수정했습니다.')
            #메세지 프레임워크
            return redirect(restaurant)
    else:
        form = RestForm(instance=restaurant)
    return render(request, 'app/rest_new.html',{
        'form': form
    })


@login_required
def rest_delete(request,id):
    restaurant = Restaurant.objects.filter(id=id).delete()
    messages.success(request, '식당을 삭제했습니다.')
    return render(request, 'app/rest_delete.html',{
        'restaurant':restaurant
    })
