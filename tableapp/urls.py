from django.urls import path
from .views import index, sort_data, search_data, pagination

urlpatterns = [
    path('', index, name="index"),
    path('sort-data', sort_data, name="sort_data"),
    path('search-data', search_data, name="search_data"),
    path('get_by_page', pagination, name="get_by_page"),
]
