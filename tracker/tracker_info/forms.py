from django import forms 

from .models import TrackingDetails 

from django.forms.widgets import NumberInput


#from django.contrib.auth import get_user_model


class DateInput(forms.DateInput):
    
    input_type = 'date'

class TrackingForm(forms.ModelForm):
    
    attempt1_date = forms.DateTimeField(label='Date & time of 1st attempt to survey the RR',required=False, widget=NumberInput(attrs={'type':'date'}))
    attempt2_date = forms.DateTimeField(label='Date & time of 2nd attempt to survey the RR', required=False, widget=NumberInput(attrs={'type':'date'}))
    attempt3_date = forms.DateTimeField(label='Date & time of 3rd attempt to survey the RR',required=False,  widget=NumberInput(attrs={'type':'date'}))
    if_rr_surveyed_date = forms.DateTimeField(label='if RR was surveyed,record the date of interview',required=False,  widget=NumberInput(attrs={'type':'date'}))
   
    class Meta:
        
        model = TrackingDetails  
        fields = [
            'HHID','Supervisor','Enumerator','RR_status','attempt1_date','attempt2_date','attempt3_date',
            
            'if_rr_surveyed_date','if_rr_not_details','status_of_RR1','HR_module_completed','HR_accompanied',
            
            'RR_module_completed','RR_accompanied','if_WER_eligible','if_WER_eligible_coompleted','WER_accompanied','if_CR_eligible',
            
            'if_CR_eligible_completed','CR_accompanied','comments','mark'
            
        ]
        
        
        
class EditTrackingForm(forms.ModelForm):
    
    attempt1_date = forms.DateTimeField(label='Date & time of 1st attempt to survey the RR',required=False, widget=NumberInput(attrs={'type':'date'}))
    attempt2_date = forms.DateTimeField(label='Date & time of 2nd attempt to survey the RR', required=False, widget=NumberInput(attrs={'type':'date'}))
    attempt3_date = forms.DateTimeField(label='Date & time of 3rd attempt to survey the RR',required=False,  widget=NumberInput(attrs={'type':'date'}))
    if_rr_surveyed_date = forms.DateTimeField(label='if RR was surveyed,record the date of interview',required=False,  widget=NumberInput(attrs={'type':'date'}))
   
    class Meta:
        
        model = TrackingDetails  
        fields = [
            'HHID','Supervisor','Enumerator','RR_status','attempt1_date','attempt2_date','attempt3_date',
            
            'if_rr_surveyed_date','if_rr_not_details','status_of_RR1','HR_module_completed','HR_accompanied',
            
            'RR_module_completed','RR_accompanied','if_WER_eligible','if_WER_eligible_coompleted','WER_accompanied','if_CR_eligible',
            
            'if_CR_eligible_completed','CR_accompanied','comments','mark'
            
        ]
    

    
        
        