from django.db import models

# Create your models here.

class Development(models.Model):
  ZONE_TYPES = [
    ('C', 'Commercial'),
    ('I', 'Industrial'),
    ('M', 'Mixed Use'),
  ]
  name = models.CharField(primary_key=True, max_length=100)
  address = models.CharField(max_length=200)
  latitude = models.DecimalField(blank=True,max_digits=15, 
    editable=False,decimal_places=9)
  longitude = models.DecimalField(blank=True,max_digits=15,
    editable=False,decimal_places=9)
  zoning_type = models.CharField(max_length=1, choices=ZONE_TYPES, default='C')
  web_url = models.URLField(max_length=100)
  img = models.ImageField(upload_to='uploads/')
  sold = models.BooleanField()
  sold_year = models.IntegerField(blank=True, null=True)
  acquired = models.IntegerField(blank=True, null=True)
  acquired_company = models.CharField(max_length=50, blank=True)
  property_text = models.TextField()
  history_text = models.TextField()
  redevelopment_text = models.TextField()
  current_status_text = models.TextField()
  property_manager_name = models.CharField(max_length=50, blank=True)
  property_manager_email = models.EmailField(max_length=254, blank=True)

  def save(self, *args, **kwargs):
    self.latitude = 0.0
    self.longitude = 0.0
    super().save(*args, **kwargs)  # Call the "real" save() method.
  
  def __str__(self):
    return self.name