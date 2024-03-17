from django.shortcuts import redirect, render
from django.urls import reverse
from author.forms import AuthorModelForm
from author.models import Author
from django.contrib.auth.decorators import login_required

# Create your views here.

def AllAuthors(request):
    authors=Author.objects.all()
    return render(request, 'author/authors.html',context={"authors": authors})

def author_details(request, id):
    author = Author.get_author_by_id(id)
    books = author.books.all()
    return render(request, 'author/author_details.html', {"author": author, "books": books})

@login_required
def create_author(request):
    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()  
            return redirect(author.show_url)

    return render(request, 'author/author_create.html', context={"form":form})

@login_required
def author_edit(request, id):
    author = Author.get_author_by_id(id)
    form = AuthorModelForm(instance=author)
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect(author.show_url)

    return render(request, 'author/author_edit.html', context={"form":form})

@login_required
def author_delete(request, id):
    author = Author.get_author_by_id(id)
    author.delete()
    return redirect('AllAuthors')