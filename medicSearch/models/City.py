'''
This model represents the cities of a state.

State (FK) and Name are required. Status is True by default.
'''
from medicSearch.models import *

class City(models.Model):
    state = models.ForeignKey(State, null=False, max_length=20, related_name='state', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.state.name)