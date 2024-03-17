from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='author/images/', null=True)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        url = reverse('AllAuthors')
        return url
    @property
    def details_url(self) -> str:
        url = reverse("author_details", args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('author_edit', args=[self.id])
        return url
    
    @classmethod
    def get_all_authors(cls):
        return cls.objects.all()
    
    @classmethod
    def create_object(cls,name, image, birthdate ):
        try:
            author = cls(name=name, image=image, birthdate=birthdate)
            print(name, image,birthdate)
            author.save()
        except Exception as e:
            print(e)
            return False
        else:
            return author

    @classmethod
    def get_author_by_id(cls, id):
        return get_object_or_404(cls, id=id)