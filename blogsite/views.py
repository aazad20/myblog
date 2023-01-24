from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    context_object_name = 'myblog'
    template_name = 'index.html'
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'details.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title','content','author']
    template_name = 'add.html'

