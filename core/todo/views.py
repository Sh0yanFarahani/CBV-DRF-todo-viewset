from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import  ListView
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Todo


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title']
    success_url  = reverse_lazy('task:task-list')
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)
    
    

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('task:task-list')


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        return self.post(request, *args, **kwargs)
    def get_queryset(self):
        return self.model.objects.all()



class TaskComplete(LoginRequiredMixin, UpdateView):
    model = Todo    
    fields = [ 
        "done", 
    ] 
    success_url= reverse_lazy('task:task-list')

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        object = self.model.objects.get(id=kwargs.get('pk'))
        object.done = True
        object.save()
        return redirect(self.success_url)
    


class TaskUpdate(UpdateView):
    model = Todo    
    fields = [ 
        "title", 
    ]
    template_name = 'todo/todo_update.html'
    success_url= reverse_lazy('task:task-list')
