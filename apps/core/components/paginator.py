from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class Paginator(pagination.PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

    def __init__(self) -> None:
        return super().__init__()

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'page_number': self.page.number,
            'page_size': self.page_size,
            'previous': self.get_previous_link(),
            'quantity_displayed': len(self.page.object_list),
            'results': data,
            'total_pages': self.page.paginator.num_pages
        })
