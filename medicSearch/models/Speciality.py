'''
This model represents the specialities that'll be attributed to Médicos profiles.

Name is required. Status is True by default.
'''
from medicSearch.models import *

class Speciality(models.Model):
    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.name)