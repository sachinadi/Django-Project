#Importing the module
from django.urls import path
from .views import healthcheck, get_books, add_book
#Include all the URL Patterns that you need for the website
urlpatterns = [
    path("health/", healthcheck),
    path("list/", get_books),
    path("add/", add_book)
]
 