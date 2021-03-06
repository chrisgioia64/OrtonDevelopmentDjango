from django.db import models
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDSOibJ9zBuUyhoacW7Y8K0vfvHcTC288E')

# Create your models here.
class Development(models.Model):
  ZONE_TYPES = [
    ('U', 'Unassigned'),
    ('C', 'Commercial'),
    ('I', 'Industrial'),
    ('M', 'Mixed Use'),
  ]
  name = models.CharField(unique=True, max_length=100)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100, blank=True, null=True)
  state = models.CharField(max_length=100, blank=True, null=True)
  zip_code = models.IntegerField(blank=True, null=True)
  REGIONS = [
    ('W', 'Western U.S.'),
    ('M', 'Midwest U.S.'),
    ('S', 'Southeast U.S.')
  ]
  region = models.CharField(max_length=1, choices=REGIONS, default='W')
  latitude = models.DecimalField(blank=True,max_digits=15, 
    editable=False,decimal_places=9)
  longitude = models.DecimalField(blank=True,max_digits=15,
    editable=False,decimal_places=9)
  zoning_type = models.CharField(max_length=1, choices=ZONE_TYPES, default='U')
  web_url = models.URLField(max_length=100, blank=True, null=True)
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

  def getFullAddress(self):
    return self.address + " " + self.city + ", " + self.state + " " + str(self.zip_code)

  def save(self, *args, **kwargs):
    geocode_result = gmaps.geocode(self.getFullAddress())
    self.latitude = 0.0
    self.longitude = 0.0
    try:
      loc = geocode_result[0]['geometry']['location']
      self.latitude = loc['lat']
      self.longitude = loc['lng']
    except Exception as err:
      print("error" + str(err))

    super().save(*args, **kwargs)  # Call the "real" save() method.
  
  def getZoningType(self):
    for abbr, detail in self.ZONE_TYPES:
      if abbr == self.zoning_type:
        return detail
    return ""

  def __str__(self):
    if self.city is not None:
      return '%20s -- (%s)' % (self.name, self.city) 
    else:
      return self.name