from django.db import models


# Author Table
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'

    def __str__(self):
        return f"{self.name}"


# Book Table
class Book(models.Model):
    id = models.AutoField(primary_key=True)  
    download_count = models.IntegerField(default=0)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = 'books_book'

    def __str__(self):
        return self.title


# Book-Authors Relationship Table
class BookAuthors(models.Model):
    id = models.AutoField(primary_key=True)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_authors')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_authors')

    class Meta:
        db_table = 'books_book_authors'


# Bookshelf Table
class Bookshelf(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

    def __str__(self):
        return self.name


# Book-Bookshelves Relationship Table
class BookBookshelves(models.Model):
    id = models.AutoField(primary_key=True)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_bookshelves')
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE, related_name='book_bookshelves')

    class Meta:
        db_table = 'books_book_bookshelves'


# Language Table
class Language(models.Model):
    id = models.AutoField(primary_key=True) 
    code = models.CharField(max_length=4)

    class Meta:
        db_table = 'books_language'

    def __str__(self):
        return self.code


# Book-Languages Relationship Table
class BookLanguages(models.Model):
    id = models.AutoField(primary_key=True)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_languages')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='book_languages')

    class Meta:
        db_table = 'books_book_languages'


# Subject Table
class Subject(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'

    def __str__(self):
        return self.name


# Book-Subjects Relationship Table
class BookSubjects(models.Model):
    id = models.AutoField(primary_key=True)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='book_subjects')

    class Meta:
        db_table = 'books_book_subjects'


# Format Table
class Format(models.Model):
    id = models.AutoField(primary_key=True) 
    mime_type = models.CharField(max_length=32)
    url = models.URLField(max_length=256)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='formats')

    class Meta:
        db_table = 'books_format'
