from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView 
from .models import Post

class IndexView(TemplateView):
	template_name = "index.html"
	model = Post

class CreatePost(CreateView):
	template_name = "core/create.html"
	model = Post

class ListPost(ListView):
	template_name = "core/"