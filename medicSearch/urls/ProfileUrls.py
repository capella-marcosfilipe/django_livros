from django.urls import path
from medicSearch.views.ProfileView import list_profile_view

urlpatterns = [
    path("", list_profile_view, name="profiles"), # Calls the method without passing an id.
    path("<int:id>", list_profile_view, name="profile"), 
]
