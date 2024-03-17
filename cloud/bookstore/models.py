from django.db import models
from django.urls import reverse

from author.models import Author

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bookstore/images/', null=True)
    author = models.CharField(max_length=100)
    price = models.IntegerField(default=10, null=True)
    numpages = models.IntegerField(default=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True) #update
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    def __str__(self):
        return f"{self.name}"
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        url = reverse('bookstore.book_details', args=[self.id])
        return url

    # @property
    # def edit_url(self):
    #     url = reverse('bookstore.book_edit', args=[self.id])
    #     return url

    