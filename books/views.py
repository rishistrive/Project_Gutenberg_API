from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from books.filters import BookFilter
from books.pagination import CustomPagination

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows books to be viewed.
    """
    queryset = Book.objects.all().order_by('-download_count')
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = BookFilter  # Add the filter class

    def get_queryset(self):
        """
        This method allows us to apply prefetching for related fields.
        This will optimize database queries for the many-to-many relationships.
        """
        queryset = super().get_queryset()

        # Use `prefetch_related` to optimize related fields fetching
        queryset = queryset.prefetch_related(
            'book_authors__author',
            'book_bookshelves__bookshelf',
            'book_languages__language',
            'book_subjects__subject',
            'formats'
        )

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_serializer_context(self):
        # Pass the request context to the serializer
        context = super().get_serializer_context()
        context.update({
            'request': self.request,
        })
        return context
