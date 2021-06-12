from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
data = {

   "Name" : "Oluwafemi Adenuga",

    "Track" : "Backend(Python)",

    "Message" : "Hi, mentor, you're doing a great job"

}
def index(request):
    return JsonResponse(data)