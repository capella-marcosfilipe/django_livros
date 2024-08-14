from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    '''
    In this class, we can add attributes that will be responsible for changing the appearance and behavior of our Profile panel in admin.
    '''
    date_hierarchy = 'created_at' # Date filter.
    list_display = ('user', 'role', 'birth', 'specialitiesList', 'addressesList') # Which columns I want to display.
    list_display_links = ('user', 'role') # Which columns from list_display I want to be clickable.
    empty_value_display = 'Vazio' # What value will show when a field is empty.
    list_filter = ('user__is_active', 'role') # Create a filter based on the fields that were added to the tuple.
    # fields = ('user', ('role', ), 'image', 'birthday', 'specialities', 'addresses') # Which fields will be shown.
    exclude = ('favorites', 'created_at', 'updated_at') # Which fields will not be shown.
    readonly_fields = ('user', ) # Which fields cannot be altered.
    search_fields = ('user__username', ) # Which fields can be used to search for an entry.
    
    # Advanced customizations
    fieldsets = ( # Grouping fields. NOTE: Cannot be used with the attribute 'fields' commented above.
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }), 
        ('Função', {
            'fields': ('role', )
        }),
        ('Para médicos', {
            'fields': ('specialities', 'addresses')
        }),
    )
    
    def birth(self, obj: 'Profile') -> None | str:
        '''
        This method cutomizes how the value for birthday will be shown in our list.
        Using .strftime, changing DateTime to formatted string if Profile.birthdat available.
        '''
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
        
    birth.empty_value_display = '__/__/__' # What shows if no birthdate is available.
    
    def specialitiesList(self, obj):
        '''
        This method customizes how the values for specialities will be shown.
        '''
        return [i.name for i in obj.specialities.all()]
    
    def addressesList(self, obj):
        '''
        This method customizes how the values for addresses will be shown.
        '''
        return [i.name for i in obj.addresses.all()]
    
    # class Media:
    #     '''
    #     This class allows us to add css and js files to our admin panel.
    #     The files must be in the static folder of our system.
    #     '''
    #     css = {
    #         'all': ('css/custom.css', )
    #     }
    #     js = ('js/custom.js', )

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)