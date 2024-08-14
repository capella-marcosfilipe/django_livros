'''
This view will let us search for doctors based on address and speciality.
'''
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>Olá mundo!</h1>', status=200)