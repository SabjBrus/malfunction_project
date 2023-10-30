from rest_framework.pagination import PageNumberPagination


class DefectsPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'limit'
