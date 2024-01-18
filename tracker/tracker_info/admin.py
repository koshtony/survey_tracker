from django.contrib import admin
from tracker_info.models import TrackingDetails,Profile

# Register your models here.
class TrackDetailsInline(admin.TabularInline):
    
    model = TrackingDetails 
    max_num = 1
    
admin.site.register(Profile) 
admin.site.register(TrackingDetails)


