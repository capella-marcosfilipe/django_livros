'''
This model represents the profiles in our system in their different roles.

ROLE_CHOICE comes from models.__init__ and they are: Admin, Médico (doctor) and Paciente (patient), being this last one default.
'''
from django.db.models import Count, Sum

from medicSearch.models import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialities = models.ManyToManyField(Speciality, blank=True, related_name='specialities')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')
    
    def __str__(self):
        return '{}'.format(self.user.username)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
        
    def show_scoring_average(self):
        """
        Shows the average of the medic's reviews.
        """
        from .Rating import Rating
        try:
            ratings = Rating.objects.filter(user_rated=self.user).aggregate(Sum('value'), Count('user'))
            if ratings['user__count'] > 0:
                scoring_average = ratings['value__sum'] / ratings['user__count']
                scoring_average = round(scoring_average, 2) # Round the value down to two decimals.
                return scoring_average
            return 'Sem avaliações'
        except:
            return 'Sem avaliações'
        