from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class TrackingDetails(models.Model):
    
    
    user = models.ForeignKey(User,on_delete = models.PROTECT)
    
    # sample details
    
    Batch = models.IntegerField(default=1,null=True)
    Sample = models.CharField(max_length=100,default="Host",null=True)
    Sample_type = models.CharField(max_length=100,default="Original",null=True,verbose_name="Sample Type")
    Stratum = models.CharField(max_length=100,default="Urban Nairobi",null=True)
    Status = models.CharField(max_length=100,default="Host",null=True)
    HHID = models.CharField(max_length=100,null=False,verbose_name="HHID/HHRID") 
    Supervisor = models.CharField(max_length=100,null=False,verbose_name="Supervisor Name")
    Enumerator = models.CharField(max_length=100,null=False,verbose_name="Enumerator Name")
    
    # Household Details
    
    HR_name = models.CharField(max_length=100,null=True,verbose_name="HR name")
    RR_name = models.CharField(max_length=100,null=True,verbose_name="RR name")
    WER_name = models.CharField(max_length=100,null=True,verbose_name="WER name")
    CR_name = models.CharField(max_length=100,null=True,verbose_name="CR name")
    
    # RR status 
    rr_choices = (("",""),("Available in Original Household","Available in Original Household"),("Available in New Household","Available in New Household"),("Not Available Relocated Locally","Not Available Relocated Locally"),("Not Available Relocated Internationally","Not Available Relocated Internationally"),("Deceased","Deceased"),("Refused to participate","Refused to participate"))
    RR_status = models.CharField(max_length=100,blank=True,verbose_name="RR status", choices=rr_choices)
    
    # RR1 Respondent 
    
    attempt1_date = models.DateTimeField(blank=True,null=True,verbose_name="Date & Time of 1st attempt to surver RR")
    attempt2_date = models.DateTimeField(blank=True,null=True,verbose_name="Date & Time of 2nd attempt to surver RR")
    attempt3_date = models.DateTimeField(blank=True,null=True,verbose_name="Date & Time of 3rd attempt to surver RR")
    if_rr_surveyed_date = models.DateField(blank=True,null=True, verbose_name="if RR was surveyed,record the date of interview")
    if_rr_not_details = models.TextField(blank=True,null=True,verbose_name="If attempts to survey the RR in their original/current household were not successful, Please record in detail the outcome from the attempts made to interview RR1 ")
    
    status_of_RR1_choices = (("",""),("Approved","Approved "),("Not Approved","Not Approved"))
    status_of_RR1 = models.CharField(max_length=100,blank=True,null=True,choices = status_of_RR1_choices, verbose_name="Status of RR1 Respondent Replacement approval [Based on feedback from column R]")
    
    # HR Module 
    HR_module_completed_choices =  (("",""),("Completed","Completed"),("Not Completed","Not Completed"))
    accompanied_by_supervisor_choices = (("",""),("Partially Accompanied","Partially Accompanied"),("Fully Accompanied","Fully Accompanied"),("Not Accompanied","Not Accompanied"))
    HR_module_completed = models.CharField(max_length=100,blank=True,null=True,choices = HR_module_completed_choices,verbose_name="Has the HR module been completed or not completed?")
    HR_accompanied = models.CharField(max_length=100,blank=True,null=True,choices = accompanied_by_supervisor_choices,verbose_name="Were you accompanied by the supervisor?")
    # RR module
    RR_module_completed_choices =  (("",""),("Completed","Completed"),("Not Completed","Not Completed"))
    RR_module_completed = models.CharField(max_length=100,blank=True,null=True,choices = RR_module_completed_choices,verbose_name='Has the RR module been completed or not completed?')
    RR_accompanied = models.CharField(max_length=100,blank=True,null=True,choices = accompanied_by_supervisor_choices,verbose_name="Were you accompanied by the supervisor?")
    #WER module 
    if_WER_eligible_choices = (("",""),("Eligible","Eligible"),("Not Eligible","Not Eligible"))
    if_WER_eligible = models.CharField(max_length=100,blank=True,null=True,choices=if_WER_eligible_choices,verbose_name = "If RR household was surveyed, was the household eligible for the WER module")
    
    if_WER_eligible_coompleted = models.CharField(max_length=100,blank=True,null=True,choices=HR_module_completed_choices, verbose_name="If eligible, has the WER module been completed or not completed?")
    WER_accompanied = models.CharField(max_length=100,blank=True,null=True,choices = accompanied_by_supervisor_choices,verbose_name="Were you accompanied by the supervisor?")
    #CR module 
    
    if_CR_eligible = models.CharField(max_length=100,blank=True,choices=if_WER_eligible_choices,verbose_name = "If RR household was surveyed, was the household eligible for the CR module") 
    if_CR_eligible_completed = models.CharField(max_length=100,blank=True,null=True,choices=HR_module_completed_choices, verbose_name="If eligible, has the CR module been completed or not completed?")
    CR_accompanied = models.CharField(max_length=100,blank=True,null=True,choices = accompanied_by_supervisor_choices,verbose_name="Were you accompanied by the supervisor?")
    # comments 
    
    comments = models.TextField(blank=True,null=True,verbose_name="Record any other comment on the household/interview") #

    # mark as finished
    
    mark = models.BooleanField(default=False,verbose_name="completed the required fields")
    
    audit = models.BooleanField(default=False,verbose_name="audit status")
    
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        
        return f'Batch: {self.Batch} supervisor:{self.Supervisor} Enumerator:{self.Enumerator} RR name: {self.RR_name}'
    
    class Meta:
        
        verbose_name = "Record"


class Supervisors(models.Model):
    
    name = models.CharField(max_length=100,default="", verbose_name="Region Name")
    supervisor = models.ForeignKey(User,related_name="supervisor_username",null=True,on_delete=models.SET_NULL)
    coordinator = models.ForeignKey(User,related_name="coordinator_username",null=True,on_delete=models.SET_NULL)
    fc = models.ForeignKey(User,null=True,related_name="field_username",verbose_name="field coordinator",on_delete=models.SET_NULL)
    
    def __str__(self):
        
        return f'Region Name: {self.name}'
    
    class Meta:
        
        verbose_name = "Surpervisor's Region"
        verbose_name_plural = "Surpervisor's Region"
    
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Supervisors,on_delete=models.SET_NULL,null=True,verbose_name="Region",related_name="region_name")
    is_supervisor = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_FC = models.BooleanField(default=False)
    image = models.ImageField(default="user.png",upload_to="profile_images")
    added_by = models.ForeignKey(User,null=True,related_name="added_by",on_delete=models.SET_NULL)
    
    def __str__(self):
        
        return f'{self.user.username} Profile'
    


    
    
    
    
    
    
    
    
    

