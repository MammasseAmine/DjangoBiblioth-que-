from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class CategoryForm(forms.ModelForm) :
  class Meta :
    model = Category
    fields = ["name"]

    widgets = {
      "name" : forms.TextInput(attrs={"class" :"form-control" })
    }



class BookForm(forms.ModelForm) :
  class Meta :
    model = Book
    fields = ["title","author","book_photo","author_photo","pages","price","rental_price_day","rental_period","total_rental","status","Category"]

    widgets = {
      "title" : forms.TextInput(attrs={"class" : "form-control"}),
      "author" : forms.TextInput(attrs={"class" : "form-control"}),
      "book_photo" : forms.FileInput(attrs={"class" : "form-control"}),
      "author_photo" : forms.FileInput(attrs={"class" : "form-control"}),
      "pages" : forms.NumberInput(attrs={"class" : "form-control"}),
      "price" : forms.NumberInput(attrs={"class" : "form-control"}),
      "rental_price_day" : forms.NumberInput(attrs={"class" : "form-control", "id" : "rentalprice"}),
      "rental_period" : forms.NumberInput(attrs={"class" : "form-control", "id" : "rentaldays"}),
      "total_rental" : forms.NumberInput(attrs={"class" : "form-control", "id" : "totalrental"}),
      "status" : forms.Select(attrs={"class" : "form-control"}),
      "Category" : forms.Select(attrs={"class" : "form-control"}),

    }

