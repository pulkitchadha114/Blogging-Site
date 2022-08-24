
from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service


def homePage(request):
    servicesData = Service.objects.all()
    print(servicesData)
    data = {'servicesData': servicesData}

    return render(request, "index.html", data)

def details(request, slug):
    serviceDetails = Service.objects.get(new_slug=slug)
    data = {'serviceDetails': serviceDetails}
    return render(request, "blogdetails.html", data)

def contact(request):
    return render(request, "contact.html")  

def saveData(request):
    return render(request, "contact.html") 