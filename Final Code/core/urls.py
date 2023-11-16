from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-todo', views.submit_todo, name='submit-todo'),
    path('complete-todo/<int:pk>/', views.complete_todo, name='complete-todo'),
    path('delete-todo/<int:pk>/', views.delete_todo, name='delete-todo'),
]
