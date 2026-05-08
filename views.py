
from .models import Listing, Entry
from django.shortcuts import render
from .models import Entry  # هذا السطر هو اللي بيحل مشكلة "is not defined"
import markdown2
import random

# 1. الصفحة الرئيسية
def index(request):
    # سحب كل المنتجات النشطة من الـ SQL
    listings = Listing.objects.all()
    return render(request, "encyclopedia/index.html", {
        "listings": listings
    })

# 2. صفحة المقال
def entry(request, title):
    article = Entry.objects.filter(title__iexact=title).first()
    if article:
        return render(request, "encyclopedia/entry.html", {
            "title": article.title,
            "content": article.content
        })
    else:
        return render(request, "encyclopedia/error.html", {"message": "المقال غير موجود"})

# 3. محرك البحث (اللي كان فيه المشكلة)
def search(request):
    query = request.GET.get('q', '')
    article = Entry.objects.filter(title__iexact=query).first()
    
    if article:
        return render(request, "encyclopedia/entry.html", {
            "title": article.title,
            "content": article.content
        })
    else:
        results = Entry.objects.filter(title__icontains=query)
        return render(request, "encyclopedia/index.html", {
            "entries": results,
            "query": query
        })

# 4. الدوال الإضافية عشان السيرفر ما يزعل
def new_page(request):
    return render(request, "encyclopedia/new.html")

def random_page(request):
    entries = Entry.objects.all()
    if entries:
        random_entry = random.choice(entries)
        return render(request, "encyclopedia/entry.html", {
            "title": random_entry.title,
            "content": random_entry.content
        })
    return render(request, "encyclopedia/index.html")