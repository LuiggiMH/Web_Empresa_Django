from django.shortcuts import render
from . models import Services

# Create your views here.
def services (request):
    services=Services.objects.all() #listando los servicios
    return render(request, "services/services.html", {'services': services})
    