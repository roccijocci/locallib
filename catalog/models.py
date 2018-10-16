from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

#models representing a book genre

class Language(models.Model):
	name_of_language = models.CharField(max_length = 200, help_text='The Language of the book is?')

	def __str__(self):
			return self.name_of_language
	

class Genre(models.Model):
	name_of_genre = models.CharField(
		max_length=200, help_text='Enter a book genre(e.g. Science Fiction)')

	def __str__(self):
		return self.name_of_genre

#model representing a book
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	#many to many fields becos genre can contain many books and books can cover many genres
	genre = models.ManyToManyField(Genre, help_text = 'Select a genre for this book')
	#one to one because a book can only have one language at a time
	language = models.ForeignKey(Language, on_delete = models.SET_NULL, null = True)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('book-detail', args= [str(self.id)])

	def display_genre(self):
		#create a string for the genre to be displayed in the Admin Area
		return ', '.join(genre.name_of_genre for genre in self.genre.all()[:3])
	display_genre.short_description = 'Genre'

#book instance model  this model represents a copy of a book.
class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique ID for this particular book across the whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	
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
	class Meta:
		ordering = ['due_back']

	def __str__(self):
		#string for representing the Model object
		# return f'{self.id} ({self.book.title})'
		return '{0} ({1}) ({2} | {3})'.format(self.id, self.book.title, self.status, self.due_back)

	@property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False
	#Author Models

class Author(models.Model):
	#models representing the author
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)
	
	class Meta:
		ordering = ['last_name', 'first_name']
		
	def get_absolute_url(self):
		#returns the url to access a particular author instance
		return reverse('author-detail',args=[str(self.id)])

	def __str__(self):
			return '{0}({1})'.format(self.last_name, self.first_name)