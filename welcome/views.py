from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello World. You're at the welcome index.")
    #return HttpResponse(request.META['REMOTE_HOST'])
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'index.html', context)

