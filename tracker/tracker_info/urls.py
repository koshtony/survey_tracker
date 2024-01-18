from django.urls import path
from . import views 
from .views import view_dashboard,add_survey_details,\
    update_survey_details,delete_survey_details, view_survey_details,\
        download_survey_details,register_user,activate_user
    
    
urlpatterns = [
    
    # Tracking details 
    path('',views.view_dashboard,name='tracker-dashboard'),
    path('add_details',views.add_survey_details,name='tracker-add-survey-details'),
    path('update_details/<int:pk>',views.update_survey_details,name='tracker-update-survey-details'),
    path('delete_details/<int:pk>',views.delete_survey_details,name='tracker-delete-survey-details'),
    path('view_details',views.view_survey_details,name='tracker-view-survey-details'),
    path('download_details',views.download_survey_details,name='tracker-download-survey-details'),
    
    # user registration 
    
    path('register_user',views.register_user,name='register-user'),
    path('activate_user',views.activate_user,name='activate-user'),
    
]

