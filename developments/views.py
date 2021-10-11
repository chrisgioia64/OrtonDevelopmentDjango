from django.shortcuts import render
from django.conf import settings

import developments
from .models import Development
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def detail(request, development_id):
  try:
    development = Development.objects.get(id=development_id)
  except Development.DoesNotExist:
    raise Http404("Development does not exist")
  return render(request, 'developments/detail.html',
          {'development' : development,
          'MEDIA_URL' : settings.MEDIA_URL})

def getFilteredDev(developments, map):
  res = []
  for dev in developments:
    found = True
    if ('region' in map):
      if (dev.region != map['region']):
        found = False
    if ('sold' in map):
      if (not dev.sold):
        found = False
    if found:
      res.append(dev)
  
  return res

def getLinkFilter(map):
  if ('sold' in map):
    return 5
  if ('region' in map):
    if (map['region'] == 'M'):
      return 2
    elif (map['region'] == 'S'):
      return 3
    else:
      return 4
  return 1

def portfolio(request):
  developments = Development.objects.all()
  map = request.GET
  filtered_developments = getFilteredDev(developments, map)
  filter = getLinkFilter(map)

  return render( request, 'developments/portfolio.html',
          {'developments' : filtered_developments,
            'MEDIA_URL' : settings.MEDIA_URL,
            'link_filter' : filter}
        )

def json(request):
  developments = Development.objects.all()
  response_data = {}
  list = []
  for development in developments:
    map = {}
    map['name'] = development.name
    map['address'] = development.address
    map['lat'] = development.latitude
    map['lng'] = development.longitude
    map['img'] = str(development.thumbnail_img)
    map['sold'] = development.sold
    map['id'] = development.id
    list.append(map)

  response_data['developments'] = list;
  return JsonResponse(response_data)

def map(request):
  return render(request, 'developments/map.html',
          {'MEDIA_URL' : settings.MEDIA_URL})

def about(request):
  return render(request, 'developments/about.html')