from django.shortcuts import render

from django.conf import settings
from django.http import Http404
from .models import *

# Create your views here.

from django.http import HttpResponse

def index(request):
  offices = Office.objects.all()
  return render(request, 'team/index.html', {
    'offices' : offices
  })

def detail(request, employee_id):
  try:
    employee = Employee.objects.get(id=employee_id)
  except Employee.DoesNotExist:
    raise Http404("Development does not exist")
  return render(request, 'team/detail.html',
          {'employee' : employee,
          'MEDIA_URL' : settings.MEDIA_URL})
  
def title(request, titleStr):
  
  employees = Employee.objects.filter(title=titleStr)
  if len(employees) == 0:
    raise Http404("No employees for title")
  return render(request, 'team/title.html',
          { 'title' : titleStr,
            'employees' : employees,
          'MEDIA_URL' : settings.MEDIA_URL})