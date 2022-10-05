from django.urls import path

from .views import add_user, user_detail

app_name = 'user'

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('user_detail/<int:pk>/', user_detail, name='user_detail')
]