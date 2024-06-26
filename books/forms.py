from django import forms
from .models import Book

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_date', 'book_cover')