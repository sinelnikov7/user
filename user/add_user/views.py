import sqlite3
import requests

from django.shortcuts import render, redirect

from .models import User

def add_user(request):
    last_user = User.objects.all().last()
    slots = ''
    need_button_add_user = True
    if last_user == None:
        need_buttons_delete_and_all_users = False
    else:
        need_buttons_delete_and_all_users = True
    if request.method == "POST":
        if last_user == None:
            number = 1
        else:
            number = last_user.id + 1
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{number}')
        if response.status_code == 200:
            name = response.json()['name']
            username = response.json()['username']
            phone = response.json()['phone']
            city = response.json()['address']['city']
            User.objects.create(name=name, username=username, phone=phone, city=city)
            need_buttons_delete_and_all_users = True
        if response.status_code == 404:
            slots = 'Больше нет данных для добовления'
            need_button_add_user = False
    context = {
        'slots': slots,
        'need_buttons_delete_and_all_users': need_buttons_delete_and_all_users,
        'need_button_add_user': need_button_add_user
    }
    return render(request, 'add_user.html', context)

def users_delete(request):
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM add_user_user')
    cursor.execute('delete from sqlite_sequence where name="add_user_user"')
    connect.commit()
    cursor.close()
    return redirect('user:add_user')

def all_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'all_users.html', context)

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user,
    }
    return render(request, 'user_detail.html', context)

