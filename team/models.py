from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

class Office(models.Model):
  name = models.CharField(unique=True, max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=20)
  zip_code = models.IntegerField()
  telephone = models.CharField(max_length=20, blank=True, null=True)
  fax = models.CharField(max_length=20, blank=True, null=True)

  def getMembers(self):
    filtered_employees = []
    employees = Employee.objects.all()
    for employee in employees:
      if employee.office == self:
        filtered_employees.append(employee)
    return filtered_employees

  def __str__(self):
    return self.name

class EmployeeType(models.Model):
  employee_type = models.CharField(max_length=200)

  def __str__(self):
    return self.employee_type

class Employee(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  description = models.TextField()
  img = models.ImageField(upload_to='img/team/', blank=True)
  university1 = models.CharField(max_length=400, blank=True)
  major1 = models.CharField(max_length=400, blank=True)
  university2 = models.CharField(max_length=400, blank=True)
  major2 = models.CharField(max_length=400, blank=True)
  office = models.ForeignKey(Office, on_delete=SET_NULL, blank=True, null=True)
  employee_type = models.ForeignKey(EmployeeType, on_delete=SET_NULL, 
  blank=True, null=True)

  def __str__(self):
    return self.first_name + " " + self.last_name