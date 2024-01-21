from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from tracker_info.models import TrackingDetails,Profile,Supervisors

# Register your models here.
class TrackingDetailsAdmin(admin.ModelAdmin):
    
    autocomplete_fields = ["user"]
    
class ProfileAdmin(admin.ModelAdmin):
    
    autocomplete_fields = ["user"]
    
class SupervisorsAdmin(admin.ModelAdmin):
    
    autocomplete_fields = ["supervisor","coordinator","fc"]
    
    
    
    
    
UserAdmin.search_fields = ("username",)
    
admin.site.register(Profile,ProfileAdmin) 
admin.site.register(Supervisors,SupervisorsAdmin)
admin.site.register(TrackingDetails,TrackingDetailsAdmin)


