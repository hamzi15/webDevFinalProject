from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from firstapp.models import Contact, Score
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    username = request.user
    return render(request, 'firstapp/index.html', {'username': username})

def scores(request):
    data = Score.objects.all
    print("HERE",data)

    username = request.user
    return render(request, 'firstapp/scores.html', {'data': data})

@csrf_exempt
def postScore(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        s = Score.objects.create(username= data['username'], moves=data['moves'], time=data['time'])
        s.save()
        return HttpResponse("ok")
    else:
        return HttpResponseBadRequest()



