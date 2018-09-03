from django.urls import path
from catalog import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), names='books'),
	path('books/<uuid:pk>',views.BookDetailView.as_view(), name = 'book-detail')
]