from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Book
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .forms import RawSearchForm
 
# -------------------------------------------------------------
def search_create_view(request):
        search_form = RawSearchForm()

        """if request.method == "POST":
                search_form = RawSearchForm(request.GET or None) 
                if search_form.is_valid():
                         return redirect('/result/')
                else:
                        print(search_form.errors)"""

        context = {
                'form' : search_form
        }
        return render(request, "search.html", context)

# -------------------------------------------------------------
def result(request):

        if request.GET:
                keyword = request.GET["keyword"]
                category = request.GET["category"]
                isAvailable = request.GET["available"]

                if isAvailable is not "":
                        isAvailable = True if isAvailable == "True" else False

                print("isAvailable 1 " + str(isAvailable))

                querySet = None
                books = None
                pagination = None

                if category and keyword and isAvailable is not "":
                        print("1")
                        querySet = Q(userId__isnull=isAvailable) & Q(category=category) & (Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(author__icontains=keyword))
                elif category and keyword: 
                        print("2") 
                        querySet = Q(category=category) & (Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(author__icontains=keyword))
                elif category and isAvailable is not "": 
                        print("3")
                        querySet = Q(category=category) & Q(userId__isnull=isAvailable)
                elif keyword and isAvailable is not "": 
                        print("4")
                        querySet =  Q(userId__isnull=isAvailable) & (Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(author__icontains=keyword))
                elif isAvailable is not "":
                        print("5")
                        querySet = Q(userId__isnull=isAvailable)
                elif category:
                        print("6")
                        querySet = Q(category=category)
                elif keyword:
                        print("7")
                        querySet = Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(author__icontains=keyword)
                else:
                        books = Book.objects.all() 
                        pagination = 10
                
                if querySet is not None:
                        books = Book.objects.filter(querySet).distinct() 
                        pagination = 1
                        
                page = request.GET.get('page')

                if books:
                        paginator = Paginator(books, pagination)
                        # Handle out of range and invalid page numbers:
                        try:
                                books = paginator.page(page)
                        except PageNotAnInteger:
                                books = paginator.page(1)
                        except EmptyPage:
                                books = paginator.page(paginator.num_pages)
                        books.url = "?category=" + category + "&available=" + str(isAvailable) + "&keyword=" + keyword

                        return render(request, 'result.html', {'books' : books})

        return render(request, 'result.html') 
