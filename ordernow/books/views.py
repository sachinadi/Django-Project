from django.shortcuts import render
from django.http import JsonResponse
from .models import Inventory
from django.views.decorators.csrf import csrf_exempt 
import json

#Defining the API
def healthcheck(request):
    return JsonResponse ({"message" : "The Server is Up and Running"})

#Create another API to get the list of books
def get_books(request):
    results = []
    books = Inventory.objects.all()
    for book in books:
        data={
            "title" : book.title,
            "price" : book.price,
            "author" : book.author
            
        }
        results.append(data)
    return JsonResponse({"books": results})

#import this decorator to exempt the API from 403 error
@csrf_exempt
def add_book(request):
    data = json.loads(request.body)
    print (data)
    book = Inventory.objects.create(
        title = data["title"],
        isbn_id = data["isbn_id"],
        price = data["price"],
        publisher = data["publisher"],
        quantity = data["quantity"],
        author= data["author"],
    )
    if book:
        return JsonResponse({"message": "Well done!! You have now added the book successfully!"})
    else:
        return "Book not added" 