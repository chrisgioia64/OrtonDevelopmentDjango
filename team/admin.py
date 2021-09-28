from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Office)
admin.site.register(Employee)
admin.site.register(EmployeeType)

