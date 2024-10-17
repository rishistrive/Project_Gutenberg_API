import django_filters
from django.db.models import Q

from .models import Book


class BookFilter(django_filters.FilterSet):
    """
    Filters for Books
    """
    gutenberg_id = django_filters.BaseInFilter(field_name='gutenberg_id', lookup_expr='in')
    language = django_filters.BaseInFilter(field_name='book_languages__language__code', lookup_expr='in')
    mime_type = django_filters.BaseInFilter(field_name='formats__mime_type', lookup_expr='in')
    author = django_filters.BaseInFilter(field_name='book_authors__author__name', lookup_expr='in')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    topic = django_filters.CharFilter(method='filter_by_topic')

    class Meta:
        model = Book
        fields = []

    def filter_by_topic(self, queryset, name, value):
        # Split the value by comma to get multiple topics
        topics = value.split(',')
        query = Q()
    
        # Build the OR conditions for each topic
        for topic in topics:
            query |= Q(book_subjects__subject__name__icontains=topic) | Q(book_bookshelves__bookshelf__name__icontains=topic)
        
        # Apply the filter and return the queryset
        return queryset.filter(query).distinct()
