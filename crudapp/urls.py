from django.urls import path
from . import views


app_name = 'crudapp'


urlpatterns = [
    path('', views.UserList, name='user_list'),
    path('create/', views.UserCreate, name='user_create'),
    path('success/', views.Create_Success, name='create_success'),
    path('update/<int:pk>/', views.UserUpdate, name='user_update'),
    path('update/success/', views.Update_Success, name='update_success'),
    path('delete/<int:pk>/', views.UserDelete, name='user_delete'),
    path('delete/success/', views.Delete_Success, name='delete_success'),
    path('detail/<int:pk>/', views.UserDetail, name='user_detail'),
]
