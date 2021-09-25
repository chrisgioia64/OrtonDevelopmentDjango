from django.db import models

# Create your models here.

class Development(models.Model):
  ZONE_TYPES = [
    ('C', 'Commercial'),
    ('I', 'Industrial'),
    ('M', 'Mixed Use'),
  ]
  name = models.CharField(unique=True, max_length=100)
  address = models.CharField(max_length=200)
  latitude = models.DecimalField(blank=True,max_digits=15, 
    editable=False,decimal_places=9)
  longitude = models.DecimalField(blank=True,max_digits=15,
    editable=False,decimal_places=9)
  zoning_type = models.CharField(max_length=1, choices=ZONE_TYPES, default='C')
  web_url = models.URLField(max_length=100)
  full_img = models.ImageField(upload_to='img/full/')
  thumbnail_img = models.ImageField(upload_to='img/thumbnail/')

  sold = models.BooleanField()
  sold_year = models.IntegerField(blank=True, null=True)
  acquired = models.IntegerField(blank=True, null=True)
  acquired_company = models.CharField(max_length=50, blank=True)
  acquired_text = models.TextField(default='', blank=True)
  property_text = models.TextField(default='', blank=True)
  history_text = models.TextField(default='', blank=True)
  redevelopment_text = models.TextField(default='', blank=True)
  current_status_text = models.TextField(default='', blank=True)

  project_manager_name = models.CharField(max_length=100, blank=True)
  project_manager_email = models.EmailField(max_length=254, blank=True)
  property_manager_name = models.CharField(max_length=100, blank=True)
  property_manager_email = models.EmailField(max_length=254, blank=True)

  def save(self, *args, **kwargs):
    self.latitude = 0.0
    self.longitude = 0.0
    super().save(*args, **kwargs)  # Call the "real" save() method.
  
  def __str__(self):
    return self.name