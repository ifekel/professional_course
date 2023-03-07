from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_url'
    
class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    login_url = 'account_url'
    permission_required = 'books.special_status'
    
class SearchResultListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_result.html'
    
    def get_queryset(self):
        return Book.objects.filter(
            Q(title__icontains='beginners') | Q(title__icontains='api')
        )
    