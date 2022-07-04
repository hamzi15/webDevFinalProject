from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from firstapp.models import Contact

# Create your views here.
def index(request):
    context = { 'name' : 'Hamza ' }
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, desc =desc)

        contact.save()
    return render(request, 'firstapp/index.html')

def scores(request):
    return render(request, 'firstapp/scores.html')

def about(request):
    # return HttpResponse("<h1>About</h1>")
    # print("yes")
    return render(request, 'firstapp/about.html')

def form(request):
    return render(request, 'firstapp/form.html')
