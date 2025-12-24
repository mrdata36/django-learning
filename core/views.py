from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'core/home.html', {'contact': contacts})