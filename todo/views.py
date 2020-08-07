from django.shortcuts import render, redirect
from django.views.generic import ListView
# Create your views here.
from .models import Todo


class TodoListView(ListView):
    model = Todo


def delete_todo(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('/')
