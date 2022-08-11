from msilib.schema import ListView
from django.shortcuts import render
from .models import Books
# Create your views here.

class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'