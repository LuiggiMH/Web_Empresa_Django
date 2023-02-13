from django.shortcuts import render

# Create your views here.

"""
Inicio - Home
Historia - About
Servicios - Services
Visitanos - Store
Contactos - Contact
Blog - Blog
Sample - Sample
"""
 
def home (request):
    return render(request, "core/home.html")

def about (request):
    return render(request, "core/about.html")

def store (request):
    return render(request, "core/store.html")

def contact (request):
    return render(request, "core/contact.html")

def sample (request):
    return render(request, "core/sample.html")