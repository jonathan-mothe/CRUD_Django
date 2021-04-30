from django.urls import path
from .views import list_author, create_author, update_author, delete_author, list_books, create_book, update_book, delete_book


urlpatterns = [
    #path('', list_author, name='list_author'),
    path('', list_books, name='list_books'),
    path('new_author', create_author, name='create_author'),
    path('new_book', create_book, name='create_book'),
    path('update_author/<int:id>/', update_author, name='update_author'),
    path('update_book/<int:id>/', update_book, name='update_book'),
    path('delete_author/<int:id>/', delete_author, name='delete_author'),
    path('delete_book/<int:id>/', delete_book, name='delete_book'),
]
