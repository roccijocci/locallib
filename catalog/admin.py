from django.contrib import admin
from catalog.models import Book, Author, Genre, BookInstance, Language

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class AuthorInline(admin.TabularInline):
		model = Book
#defining  custom admin class
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name','last_name',('date_of_birth','date_of_death')]
	inlines = [AuthorInline]
#register the admin class with the associated class Name(models.Model):
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title','author','display_genre')
	inlines = [BooksInstanceInline]
#Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	fieldsets = (
			(None, {
					"fields": (
						'book',
						'imprint',
						'id'	
					)
			}),
			('Availability', {
				'fields': (
					'status',
					'due_back'
				)
			})
	)