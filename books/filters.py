from typing import override
from django.db.models import QuerySet
from django.utils.datastructures import MultiValueDict
from django_filters import rest_framework as filters

from books.models import Book


class BaseFilter(filters.BaseInFilter):

    @override
    def filter(self, qs: QuerySet, value: MultiValueDict) -> QuerySet:
        raise NotImplementedError(
            f"Subclasses must implement this method using params {value} and {qs}"
        )


class TitleFilter(BaseFilter):

    @override
    def filter(self, qs: QuerySet, value: MultiValueDict) -> QuerySet:
        return qs.filter(title__icontains=value)


class AuthorFilter(BaseFilter):

    @override
    def filter(self, qs: QuerySet, value: MultiValueDict) -> QuerySet:
        return qs.filter(author__icontains=value)


class PublishedDateFilter(BaseFilter):

    @override
    def filter(self, qs: QuerySet, value: MultiValueDict) -> QuerySet:
        return qs.filter(published_date=value)


class GenreFilter(BaseFilter):

    @override
    def filter(self, qs: QuerySet, value: MultiValueDict) -> QuerySet:
        return qs.filter(genre=value)


class BookFilter(filters.FilterSet):
    # Define filters as class attributes
    filters: dict[str, type] = {
        "title": TitleFilter,
        "author": AuthorFilter,
        "published_date": PublishedDateFilter,
        "genre": GenreFilter,
    }

    class Meta:
        model = Book
        fields = []

    def apply_filters(self, qs: QuerySet, params: MultiValueDict) -> QuerySet:
        for key, value in params.items():
            if key in self.filters:
                qs = self.filters[key]().filter(qs, value)
        return qs
