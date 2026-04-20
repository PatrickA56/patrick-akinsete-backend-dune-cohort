from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("""
    <h1> Welcome to torilo shop</h1>
    <p> your one stop online store for quality products at great prices </p>
    <a href='/products/'>Browse Products</a>
    """)


def product_list(request):
    return HttpResponse("""
    <h1> Our Products </h1>
    <ul>
    <li>product 1; premium Backpack- $40</li>
    <li>product 2; premium Backpack- $40</li>
    <li>product 3; premium Backpack- $40</li>
    </ul>
    <a href='/'>Home</a>
    """)


def about(request):
    return HttpResponse("""
    <h1>About Toriloshop</h1>
    <p>Toriloshop was foundd in 2026 to make online shopping simple</p>
    <a href='/'>Home</a>
    """)

def custom_404(request, exception):
    return render(request, "404.html", {})