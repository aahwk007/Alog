from django.urls import path
from . import views


urlpatterns = [
    path('', views.gettodos),
    path('todo/<str:pk>/', views.gettodo),
    path('create-todo', views.create_todo),
    path('update-todo/<str:pk>/', views.update_todo),
    path('delete-todo/<str:pk>/', views.delete_todo)

]
