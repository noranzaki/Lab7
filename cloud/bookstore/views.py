from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from bookstore.models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'bookstore/index.html')

def AllBooks(request):
    books=Book.objects.all()
    return render(request, 'bookstore/books.html',context={"books": books})


def book_details(request,id):
    book=Book.objects.get(id=id)
    return render(request,'bookstore/book_details.html',context={"book":book})

@login_required
def book_edit(request, id):
    book=Book.objects.get(id=id)
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        book.name = request.POST["name"]
        book.author = request.POST["author"]
        book.price = request.POST['price']
        book.numpages = request.POST['numpages']
        book.image = request.FILES['image']
        book.save()

        url = reverse("AllBooks")
        return redirect(url)

    return render(request, 'bookstore/book_edit.html',context={"book":book})

@login_required
def book_delete(request, id):
    book= Book.objects.get(id=id)
    book.delete()
    url = reverse("AllBooks")
    return redirect(url)