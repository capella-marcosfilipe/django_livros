from django.db.models import Q
from django.shortcuts import render

from medicSearch.models import Profile


def list_medics_view(request):
    # Possible filters
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")
    
    medics = Profile.objects.filter(role=2) #role=2 represents  doctors.
    
    # Filtering after the parameters given in the query.
    if name is not None and name != "":
        medics = medics.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))
    if speciality is not None:
        medics = medics.filter(specialities__id=speciality)
    
    # City is contained in Neighborhood and State is contained in City
    if neighborhood is not None:
        medics = medics.filter(addresses_neighborhood=neighborhood)
    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)
    
    # Dictionary containing the result of the query. Context is the data that can be accessed by our template.
    context = {
        'medics': medics
    }
    
    return render(request, template_name='medic/medics.html', context=context, status=200)
    