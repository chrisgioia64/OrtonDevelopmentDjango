from django.shortcuts import render
from .models import Development
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("main page")

def detail(request, development_id):
  try:
    development = Development.objects.get(id=development_id)
  except Development.DoesNotExist:
    raise Http404("Development does not exist")
  return render(request, 'developments/detail.html',
          {'development' : development})