from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция для отображения домашней страницы
    """
    # Генерация кол-тв некотороых главных обьектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Sessions
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    """ 
    Доступные книги (status = 'a')
    """
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.all().count() # Метол all() применен по умолчанию
    num_genres = Genre.objects.count()

    # Отрисовка HTML-шаблона index.html c данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_abailable': num_instances_available,
                 'num_authors': num_authors, 'num_genres': num_genres,
                 'num_visits': num_visits},
    )

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains="Jamila")[:5]
    template_name = 'books/book_list.html'
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'authors/author_list.html'
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author