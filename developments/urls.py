from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  # path('', views.index, name='index'),
  path('<int:development_id>/', views.detail, name='detail'),
  path('portfolio/', views.portfolio, name='portfolio'),
  # path('map/', views.map, name='map')
  path('developments.json', views.json, name='json'),
  path('', views.map, name='map'),
  path('about/', views.about, name='about'),
]