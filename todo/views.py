from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Todo


class TodoListView(ListView):
    model = Todo
