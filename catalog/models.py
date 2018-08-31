from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

#models representing a book genre
class Genre(models.Model):
	name_of_genre = models.CharField(max_length=200, help_text='Enter a book genre(e.g. Science Fiction)')

def __str__(self):
		return self.name_of_genre


#model representing a book
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.ChaarField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	#many to many fields becos genre can contain many books and books can cover many genres
	genre = models.ManyToManyField(Genre, help_text = 'Select a genre for this book')

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('book-detail', args= [str(self.id)])

#book instance model  this model represents a copy of a book.
class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique ID for this particular book across the whole library')
	book = models.ForeignKeyField('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.Charfield(max_length=200)
	due_back = models.DateField(null=True, blank=True)
	
	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r','Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text = 'Book Availability'
	)
		
		def __str__(self):
				return 

		def __unicode__(self):
				return 
