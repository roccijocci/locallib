from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author , BookInstance, Genre

# Create your views here.
class BookListView(generic.ListView):
		model = Book
		context_object_name = 'booksview'
		queryset = Book.objects.filter(title__icontains='Master')[:5]
		template_name = "books/book_list.html"

		def get_context_data(self,**kwargs):
			context = super(BookListView, self).get_context_data(**kwargs)
			context['some_data'] = 'This is just some data'
			return context

class BookDetailView(generic.DetailView):
		model = Book
		# template_name=''
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