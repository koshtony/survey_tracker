from django.shortcuts import render
from django.http import JsonResponse,FileResponse
from django.contrib.auth.models import User
from django.conf import settings
from.forms import TrackingForm,EditTrackingForm
from .models import TrackingDetails
from .load_data import lookup_hhid,export_data
from datetime import datetime as datetime
import os

# Create your views here.

def view_dashboard(request):
    
    trackings = TrackingDetails.objects.all()
    
    context = {"trackings":trackings}
    
    return render(request,'tracker_info/dashboard.html',context)

def add_survey_details(request):
    
    form = TrackingForm()
    
    if request.POST:
        
        sub_form = TrackingForm(request.POST)
        
        if sub_form.is_valid():
            
            hhid = sub_form.cleaned_data.get("HHID")
            supervisor = sub_form.cleaned_data.get("Supervisor")
            enum = sub_form.cleaned_data.get("Enumerator")
            rr_status = sub_form.cleaned_data.get("RR_status")
            attempt1_date = sub_form.cleaned_data.get("attempt1_date")
            attempt2_date = sub_form.cleaned_data.get("attempt2_date")
            attempt3_date = sub_form.cleaned_data.get("attempt3_date")
            if_rr_surveyed_date = sub_form.cleaned_data.get("if_rr_surveyed_date")
            if_rr_not_details  = sub_form.cleaned_data.get("if_rr_not_details")
            status_of_RR1 = sub_form.cleaned_data.get("status_of_RR1")
            HR_module_completed = sub_form.cleaned_data.get("HR_module_completed")
            RR_module_completed = sub_form.cleaned_data.get("RR_module_completed")
            if_WER_eligible = sub_form.cleaned_data.get("if_WER_eligible")
            if_WER_eligible_coompleted = sub_form.cleaned_data.get("if_WER_eligible_coompleted")
            if_CR_eligible = sub_form.cleaned_data.get("if_CR_eligible")
            if_CR_eligible_completed = sub_form.cleaned_data.get("if_CR_eligible_completed")
            comments = sub_form.cleaned_data.get("comments")
            mark = sub_form.cleaned_data.get("mark")
            print("attempt1 "+str(attempt1_date))
            if attempt1_date!=None:
                
                attempt1_date = datetime.combine(attempt1_date,datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S").time())
                print(attempt1_date)
            elif attempt2_date!=None:
                
                attempt2_date = datetime.combine(attempt2_date,datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S").time())
            elif attempt3_date!=None:
                
                attempt3_date = datetime.combine(attempt3_date,datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S").time())
                
            else:
                
                attempt1_date = attempt1_date 
            
            
            try:
               if len(lookup_hhid(int(hhid)))>=1:
                    data_dict = lookup_hhid(int(hhid))[0]
               elif len(lookup_hhid(int(hhid)))==0:
                   JsonResponse("No matching HHID details found",safe=False)
               
                   
               
            except:
                
                return JsonResponse("failed to lookup HHID! re-check",safe=False)
            
            tracking_ = TrackingDetails(
                
                user = User.objects.get(username="koshtech"), Batch = data_dict["Batch"], Sample = data_dict["Sample"],
                
                Sample_type = data_dict["Sample Type"],Stratum = data_dict["Stratum"],
                
                Status = data_dict["Status"],HHID = hhid, Supervisor = supervisor,
                
                Enumerator = enum , HR_name = data_dict["HR name"], RR_name = data_dict["RR name"],
                
                WER_name = data_dict["WER name"],CR_name = data_dict["CR name"], 
                
                RR_status = rr_status , attempt1_date = attempt1_date, attempt2_date=attempt2_date,
                
                attempt3_date = attempt3_date , if_rr_surveyed_date=if_rr_surveyed_date, 
                
                if_rr_not_details = if_rr_not_details, status_of_RR1=status_of_RR1,HR_module_completed=HR_module_completed,
                
                RR_module_completed = RR_module_completed, if_WER_eligible=if_WER_eligible,if_WER_eligible_coompleted=if_WER_eligible_coompleted,
                
                if_CR_eligible=if_CR_eligible,if_CR_eligible_completed=if_CR_eligible_completed,
                
                comments = comments, mark = mark , last_updated = datetime.now()
                
                
                
                
                
                
                
                
                
                
            )
            tracking_.save()
                
                
            
            
            
            
            return JsonResponse("info addedd",safe=False)
    
    context = {"form":form}
    
    return render(request,'tracker_info/add_record.html',context)

def update_survey_details(request,pk):
    
    tracking_detail = TrackingDetails.objects.get(pk=pk)
    
    form = EditTrackingForm(instance=tracking_detail)
    
    context = {"form":form, "pk":pk}
    
    if request.POST:
        
        edit_form = EditTrackingForm(request.POST,instance=tracking_detail)
        
        edit_form.save()
        
        return JsonResponse("info updated",safe=False)
    
    
    
    return render(request,'tracker_info/edit_record.html',context)

def delete_survey_details(request,pk):
    
    pass 

def view_survey_details(request):
    
    trackings = TrackingDetails.objects.all()
    
    context = {"trackings":trackings}
    
    return render(request,'tracker_info/view_data.html',context)

def download_survey_details(request):
    
    filename = "tracking_sheet_details.xlsx"
    filepath = os.path.join(settings.MEDIA_ROOT,filename)
    
    export_data(filepath)
    
    path = open(filepath,'rb')
    
    response = FileResponse(path,as_attachment=True)
    
    return response
    
    
    