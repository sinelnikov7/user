from django.shortcuts import render

import requests

from .models import User


def add_user(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    if request.method == "POST":
        last_user = User.objects.all().last()
        if last_user == None:
            number = 1
        else:
            number = last_user.id + 1
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{number}')
        name = response.json()['name']
        username = response.json()['username']
        phone = response.json()['phone']
        city = response.json()['address']['city']
        User.objects.create(name=name, username=username, phone=phone, city=city)
    return render(request, 'add_user.html', context)

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user,
    }
    return render(request, 'user_detail.html', context)

