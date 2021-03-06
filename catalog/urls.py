from django.urls import path, re_path
from catalog import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name ='books'),
	re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
	
	path('authors/', views.AuthorListView.as_view(),  name = 'authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

	path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
	path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name= 'borrowed'),
]
