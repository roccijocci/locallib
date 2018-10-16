from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author , BookInstance, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def index(request):
	# view function for homepage of site

	#Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	#num AvailableBooks (status = 'a')
	num_instances_available = BookInstance.objects.filter(
		status__exact='a').count()

	num_authors = Author.objects.count()
	# Number of visits to this view, as counted by the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	num_genres = Genre.objects.all().count()

	# num_of_books_with_a = Author.objects.filter(last_name__exact="James").count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_genres': num_genres,
		'num_visits': num_visits,
		# 'num_of_books_with_a': num_of_books_with_a
	}

	return render(request, 'index.html', context=context)



class BookListView(generic.ListView):
		model = Book
		context_object_name = 'book_list'
		# queryset = Book.objects.filter(title__icontains='Master')[:5]
		queryset = Book.objects.all()
		template_name = "books/book_list.html"

		def get_context_data(self,**kwargs):
			context = super(BookListView, self).get_context_data(**kwargs)
			return context


class AuthorListView(generic.ListView):
		model = Author
		context_object_name = 'author_list'
		queryset = Author.objects.all()
		template_name = 'authors/author_list.html'

		def get_context_data(self, **kwargs):
			context = super(AuthorListView, self).get_context_data(**kwargs)
			return context



class BookDetailView(generic.DetailView):
		model = Book
		# template_name=''

class AuthorDetailView(generic.DetailView):
		model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
	#generic class-based view listing books on loan to current user
		model = BookInstance
		template_name = 'catalog/bookinstance_list_borrowed_user.html'
		paginate_by = 5

		def get_queryset(self):
				return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
		
