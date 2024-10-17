from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthors)
admin.site.register(Bookshelf)
admin.site.register(BookBookshelves)
admin.site.register(Language)
admin.site.register(BookLanguages)
admin.site.register(Subject)
admin.site.register(BookSubjects)
admin.site.register(Format)