from django.urls import path, re_path
from catalog import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name ='books'),
	path('authors/', views.AuthorListView.as_view(),  name = 'authors'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
