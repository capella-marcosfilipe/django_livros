'''
This model represents the addresses the doctors attend patients.

Required fields are: Name and Address.
Neighborhood is a Foreign Key and can be null.
Status is True by default.
Other fields are optional.
'''
from medicSearch.models import *

class Address(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, null=True, related_name='neighborhood', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=20)
    address = models.CharField(null=False, max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    days_week = models.ManyToManyField(DayWeek, blank=True, related_name='dawys_week')
    phone = models.CharField(null=True, blank=True, max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    