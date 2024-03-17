from django.urls import path
from bookstore import views

urlpatterns = [
    path('home', views.home, name='home' ),
    path('AllBooks', views.AllBooks, name='AllBooks' ),
    path('<int:id>', views.book_details, name='bookstore.book_details'),
    path('<int:id>/edit', views.book_edit, name='bookstore.book_edit'),
    path('<int:id>/delete', views.book_delete, name='bookstore.book_delete'),

] 