from django.shortcuts import render,redirect
from .models import Book

def home(request):
    books = Book.objects
    return render(request, 'home.html', {'books' : books})
def submitt(request):
    s = Book()
    s.message = request.GET['message']
    s.pub_person = request.GET['pub_person']
    s.pub_date = request.GET['pub_date']
    s.save()
    return redirect('/')