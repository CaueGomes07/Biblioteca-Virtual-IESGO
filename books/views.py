from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from django.template import loader
#from .forms import RegistroForm


# Create your views here.
def bookList(request):
    template = loader.get_template('book_list.html')
    books = Book.objects.all()
    context = {
        'books': books,
        'title': 'Estante Virtual'
        }
    return HttpResponse(template.render(context, request))
