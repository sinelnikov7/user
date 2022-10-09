from django.urls import path

from .views import add_user, user_detail, users_delete, all_users

app_name = 'user'

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('user_detail/delete/', users_delete, name='users_delete'),
    path('user_detail/all_users/', all_users, name='all_users'),
    path('user_detail/<int:pk>/', user_detail, name='user_detail'),
]