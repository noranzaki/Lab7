from django.urls import path
from author import views

urlpatterns = [
    path('AllAuthors', views.AllAuthors, name='AllAuthors' ),
    path('<int:id>', views.author_details, name='author_details'),
    path('createAuthor', views.create_author, name='author_create'),
    path('<int:id>/edit', views.author_edit, name='author_edit'),
    path('<int:id>/delete', views.author_delete, name='author_delete'),

] 