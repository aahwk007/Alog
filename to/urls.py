from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/<str:pk>/', views.todo, name='todo'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('update-todo/<str:pk>/', views.update_todo, name='update-todo'),
    path('delete-todo/<str:pk>', views.delete_todo, name='delete-todo'),
]
