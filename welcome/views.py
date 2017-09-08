from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    #return HttpResponse("Hello World. You're at the welcome index.")
    #return HttpResponse(request.META['REMOTE_HOST'])
    message = models.Message(username = "user1", password = "p1")
    message.save()

    msg1 = models.Message.objects.get(username = "user1")

    context = {}
    #context['hello'] = 'Hello World'
    context['hello'] = msg1.password
    return HttpResponse(msg1.password)
    #return render(request, 'index.html', context)



