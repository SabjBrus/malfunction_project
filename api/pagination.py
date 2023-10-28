from rest_framework.pagination import PageNumberPagination


class DefectsPagination(PageNumberPagination):
    page_size = 3
