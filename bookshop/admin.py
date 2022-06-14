from django.contrib import admin
from .models import Author, Genre, Book 
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_filter = ('last_name', ) #кортеж ставить запятую


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','description','author', 'amount',  'price')
    list_filter = ('author', ) #кортеж ставить запятую
      


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
