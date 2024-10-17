from rest_framework import serializers

from .models import (Author, Book, BookAuthors, BookBookshelves, BookLanguages,
                     Bookshelf, BookSubjects, Format, Language, Subject)


# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year', 'death_year']


# Bookshelf Serializer
class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['id', 'name']


# Language Serializer
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code']


# Format Serializer
class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['id', 'mime_type', 'url']


# Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    """
    authors = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'download_count', 'gutenberg_id', 'media_type', 'authors', 'bookshelves', 'languages', 'subjects', 'formats']

    # Serializer method to get the authors from BookAuthors relationship
    def get_authors(self, obj):
        book_authors = BookAuthors.objects.filter(book=obj)
        authors_queryset = [ba.author for ba in book_authors]

        # Get the author from the request
        author_param = self.context['request'].query_params.get('author', None)

        # If an author parameter is provided, filter the authors accordingly
        if author_param:
            author_list = author_param.split(',')  
            authors_queryset = [author for author in authors_queryset 
                                if any(param.lower() in author.name.lower() for param in author_list)]

        return AuthorSerializer(authors_queryset, many=True).data

    # Serializer method to get the bookshelves from BookBookshelves relationship
    def get_bookshelves(self, obj):
        book_bookshelves = BookBookshelves.objects.filter(book=obj)
        bookshelves_queryset = [bb.bookshelf for bb in book_bookshelves]
        
        # Get the topic from the request
        topic_param = self.context['request'].query_params.get('topic', None)
        
        # If a topic is provided, filter the bookshelves accordingly
        if topic_param:
            topic_list = topic_param.split(',') 
            bookshelves_queryset = [bookshelf for bookshelf in bookshelves_queryset 
                                    if any(param.lower() in bookshelf.name.lower() for param in topic_list)]

        return BookshelfSerializer(bookshelves_queryset, many=True).data

    # Serializer method to get the languages from BookLanguages relationship
    def get_languages(self, obj):
        book_languages = BookLanguages.objects.filter(book=obj)
        languages_queryset = [bl.language for bl in book_languages]
        
        # Get the language from the request
        language_param = self.context['request'].query_params.get('language', None)

        # If a language parameter is provided, filter the languages accordingly
        if language_param:
            language_list = language_param.split(',')  # Split by comma
            languages_queryset = [language for language in languages_queryset 
                                  if any(param.lower() in language.code.lower() for param in language_list)]

        return LanguageSerializer(languages_queryset, many=True).data

    # Serializer method to get the subjects from BookSubjects relationship
    def get_subjects(self, obj):
        book_subjects = BookSubjects.objects.filter(book=obj)
        subjects_queryset = [bs.subject for bs in book_subjects]
        
        # Get the topic from the request
        topic_param = self.context['request'].query_params.get('topic', None)

        # If a topic is provided, filter the subjects accordingly
        if topic_param:
            topic_list = topic_param.split(',')  # Split by comma
            subjects_queryset = [subject for subject in subjects_queryset 
                                 if any(param.lower() in subject.name.lower() for param in topic_list)]

        return SubjectSerializer(subjects_queryset, many=True).data

    def get_formats(self, obj):
        # Get the MIME type from the request
        mime_type_param = self.context['request'].query_params.get('mime_type', None)
        formats_queryset = obj.formats.all()

        # If a mime_type is provided, filter the formats accordingly
        if mime_type_param:
            mime_type_list = mime_type_param.split(',')  # Split by comma
            formats_queryset = formats_queryset.filter(mime_type__in=[m for m in mime_type_list if m])

        return FormatSerializer(formats_queryset, many=True).data