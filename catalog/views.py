from django.shortcuts import render
from catalog.models import Book, Author , BookInstance, Genre

# Create your views here.
def index(request):
	# view function for homepage of site
	
	#Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	
	#num AvailableBooks (status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	
	num_authors = Author.objects.count()

	num_genres = Genre.objects.all().count()

	# num_of_books_with_a = Author.objects.filter(last_name__exact="James").count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_genres': num_genres,
		# 'num_of_books_with_a': num_of_books_with_a
	}

	return render(request,'index.html',context=context)