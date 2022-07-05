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
    all_items = Score.objects.filter(username=request.user)
    


    data = {}
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
    data = {
        "zero": {"username" : "", "moves" : "", "time" : ""},
        "one": {"username" : "", "moves" : "", "time" : ""},
        "two": {"username" : "", "moves" : "", "time" : ""},
        "three": {"username" : "", "moves" : "", "time" : ""},
        "four": {"username" : "", "moves" : "", "time" : ""},
        "five": {"username" : "", "moves" : "", "time" : ""},
        "six": {"username" : "", "moves" : "", "time" : ""},
        "seven": {"username" : "", "moves" : "", "time" : ""},
        "eight": {"username" : "", "moves" : "", "time" : ""},
        "nine": {"username" : "", "moves" : "", "time" : ""},
        "ten": {"username" : "", "moves" : "", "time" : ""},
    }
    for i in range(len(all_items)):
        if i > 9:
            break 
        data[numbers[i]] = {"username": all_items[i].username, "moves": all_items[i].moves, "time": all_items[i].time}
    print(data)

    return render(request, 'firstapp/scores.html', data)

@csrf_exempt
def postScore(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        s = Score.objects.create(username= data['username'], moves=data['moves'], time=data['time'])
        s.save()
        return HttpResponse("ok")
    else:
        return HttpResponseBadRequest()



