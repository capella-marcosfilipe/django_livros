'''
This file communicates to Django what models should reflect on our database structure.
'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# To be used in models with "role" attribute.
ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

# Models in use:
from .Rating import Rating
from .DayWeek import DayWeek
from .State import State
from .City import City
from .Neighborhood import Neighborhood
from .Address import Address
from .Speciality import Speciality
from .Profile import Profile