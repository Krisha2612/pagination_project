from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 5)  # Show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {'page_obj': page_obj, 'query': query})

# Create your views here.
