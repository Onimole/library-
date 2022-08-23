from msilib.schema import ListView
from django.shortcuts import render
from .models import Book
from rest_framework import generics

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    model = Book
    template_name = 'book_list.html'