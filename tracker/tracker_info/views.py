from django.shortcuts import render
from django.http import JsonResponse,FileResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from.forms import TrackingForm,EditTrackingForm
from .models import TrackingDetails,Profile
from .load_data import lookup_hhid,export_data
from datetime import datetime as datetime,timedelta
import os

# Create your views here.
@login_required
def view_dashboard(request):
    #print(request.user.profile.supervisor)
    complete = 0
    all = 0 
    incomplete = 0
    if Profile.objects.filter(user__username=request.user.username).exists():
        if request.user.profile.is_supervisor:
           
            trackings = TrackingDetails.objects.filter(user__profile__region__supervisor__username = request.user.username).order_by('last_updated')
            print(trackings)
            complete += len(TrackingDetails.objects.filter(user__profile__region__supervisor__username = request.user.username,mark=True))
            all += len(trackings)
            incomplete += all - complete
            
            
        elif request.user.profile.is_coordinator:
            
            trackings = TrackingDetails.objects.filter(user__profile__region__coordinator__username = request.user.username).order_by('last_updated')
            print(trackings)
            complete += len(TrackingDetails.objects.filter(user__profile__region__coordinator__username = request.user.username,mark=True))
            all += len(trackings)
            incomplete += all - complete
            
            
        elif request.user.profile.is_FC:
            
            trackings = TrackingDetails.objects.filter(user__profile__region__fc__username = request.user.username).order_by('last_updated')
            print(trackings)
            complete += len(TrackingDetails.objects.filter(user__profile__region__fc__username = request.user.username,mark=True))
            all += len(trackings)
            incomplete += all - complete
            
       
        elif request.user.is_superuser:
            
            trackings = TrackingDetails.objects.all()
            complete += len(TrackingDetails.objects.filter(mark=True))
            all += len(TrackingDetails.objects.all())
            incomplete += all - complete
            
        else:
            trackings = TrackingDetails.objects.filter(user__username = request.user.username)
            complete += len(TrackingDetails.objects.filter(user__username = request.user.username,mark=True))
            incomplete += len(TrackingDetails.objects.filter(user__username = request.user.username,mark=False))
            all += complete + incomplete
    else:
        trackings = TrackingDetails.objects.filter(user__username = request.user.username)
        complete += len(TrackingDetails.objects.filter(user__username = request.user.username,mark=True))
        incomplete += len(TrackingDetails.objects.filter(user__username = request.user.username,mark=False))
        all += complete + incomplete
        
        
        
        
            
                        
    
    context = {"trackings":trackings,"complete":complete,"incomplete":incomplete,"mytotal":complete+incomplete,"all":all}
    
    return render(request,'tracker_info/dashboard.html',context)

@login_required
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
            now = datetime.now()+timedelta(hours=3)
            print(supervisor)
            if attempt1_date!=None:
                
                attempt1_date = datetime.combine(attempt1_date,datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
                
            elif attempt2_date!=None:
                
                attempt2_date = datetime.combine(attempt2_date,datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
            elif attempt3_date!=None:
                
                attempt3_date = datetime.combine(attempt3_date,datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
                
            else:
                
                attempt1_date = attempt1_date 
            
            
            try:
                
               
                    data_dict = lookup_hhid(int(hhid))[0]
               
            except:
                
                return JsonResponse("failed to lookup HHID! re-check",safe=False)
            
            tracking_ = TrackingDetails(
                
                user = request.user, Batch = data_dict["Batch"], Sample = data_dict["Sample"],
                
                Sample_type = data_dict["Sample Type"],Stratum = data_dict["Stratum"],
                
                Status = data_dict["Status"],HHID = hhid, Supervisor = supervisor,
                
                Enumerator = enum , HR_name = data_dict["HR name"], RR_name = data_dict["RR name"],
                
                WER_name = data_dict["WER name"],CR_name = data_dict["CR name"], 
                
                RR_status = rr_status , attempt1_date = attempt1_date, attempt2_date=attempt2_date,
                
                attempt3_date = attempt3_date , if_rr_surveyed_date=if_rr_surveyed_date, 
                
                if_rr_not_details = if_rr_not_details, status_of_RR1=status_of_RR1,HR_module_completed=HR_module_completed,
                
                RR_module_completed = RR_module_completed, if_WER_eligible=if_WER_eligible,if_WER_eligible_coompleted=if_WER_eligible_coompleted,
                
                if_CR_eligible=if_CR_eligible,if_CR_eligible_completed=if_CR_eligible_completed,
                
                comments = comments, mark = mark , last_updated = datetime.now()+timedelta(hours=3)
                
                
                
                
                
                
                
                
                
                
            )
            tracking_.save()
                
                
            
            
            
            
            return JsonResponse("info added successfully",safe=False)
    
    context = {"form":form}
    
    return render(request,'tracker_info/add_record.html',context)

@login_required
def update_survey_details(request,pk):
    
    tracking_detail = TrackingDetails.objects.get(pk=pk)
    
    tracking_filt = TrackingDetails.objects.filter(pk=pk)[0]
    
    form = EditTrackingForm(instance=tracking_detail)
    
    context = {"form":form, "pk":pk,"tracking":tracking_detail}
    
    now = datetime.now()+timedelta(hours=3)
    
    if request.POST:
        
        edit_form = EditTrackingForm(request.POST,instance=tracking_detail)
        edit_commit = edit_form.save(commit=False)
        
        if edit_form.is_valid():
            
            #print(datetime.combine(edit_form.cleaned_data.get("attempt2_date"),datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S").time()))
        
            if tracking_filt.attempt1_date!=None:
                
                edit_commit.attempt1_date = tracking_filt.attempt1_date
                
            elif edit_form.cleaned_data.get("attempt1_date")!=None:
                
                edit_commit.attempt1_date=datetime.combine(edit_form.cleaned_data.get("attempt1_date"),datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
                
                
            
            if tracking_filt.attempt2_date!=None:
                
                edit_commit.attempt2_date = tracking_filt.attempt2_date
                
            elif edit_form.cleaned_data.get("attempt2_date")!=None:
                
                edit_commit.attempt2_date=datetime.combine(edit_form.cleaned_data.get("attempt2_date"),datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
                
            
            if tracking_filt.attempt3_date!=None:
                
                edit_commit.attempt3_date = tracking_filt.attempt3_date
                
            elif edit_form.cleaned_data.get("attempt3_date")!=None:
                
                edit_commit.attempt3_date=datetime.combine(edit_form.cleaned_data.get("attempt3_date"),datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
                
            if tracking_filt.if_rr_surveyed_date!=None:
                
                edit_commit.if_rr_surveyed_date = tracking_filt.if_rr_surveyed_date
                
            elif edit_form.cleaned_data.get("if_rr_surveyed_date")!=None:
                
                edit_commit.if_rr_surveyed_date=datetime.combine(edit_form.cleaned_data.get("if_rr_surveyed_date"),datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").time())
            
                
            edit_commit.last_updated = datetime.now()+timedelta(hours=3)
            
            edit_commit.save()
            
            return JsonResponse("info updated successfully",safe=False)
    
    
    
    return render(request,'tracker_info/edit_record.html',context)

@login_required
def delete_survey_details(request,pk):
    
    pass 

@login_required 
def mark_as_complete(request):
    
    if request.POST:
        
        pks = request.POST.get("pks").split(',')
        action = request.POST.get("action")
        status = ""
        
            
        if action == "complete":
            for pk in pks:
                tracking = TrackingDetails.objects.get(pk=int(pk))
                tracking.mark = True 
                tracking.save()
                
            status+="marked as complete successfully"
                
        elif action == "incomplete":
            for pk in pks:   
                tracking = TrackingDetails.objects.get(pk=int(pk))
                tracking.mark = False
                tracking.save()
            status+="marked as incomplete successfully"
                
        elif action == "delete":
            for pk in pks:
                tracking = TrackingDetails.objects.get(pk=int(pk))
                tracking.delete()
            status+="Deleted successfully"
        else:
            
            status+="Action not recognised"
                
            
                
                
                
        
        return JsonResponse(status,safe=False)

@login_required
def view_survey_details(request):
    
    if Profile.objects.filter(user__username=request.user.username).exists():
        if request.user.profile.is_supervisor:
           
            trackings = TrackingDetails.objects.filter(user__profile__region__supervisor__username = request.user.username).order_by('last_updated')
        
        elif request.user.profile.is_coordinator:
            
            trackings = TrackingDetails.objects.filter(user__profile__region__coordinator__username = request.user.username).order_by('last_updated')
           
 
        elif request.user.profile.is_FC:
            
            trackings = TrackingDetails.objects.filter(user__profile__region__fc__username = request.user.username).order_by('last_updated')
          
        elif request.user.is_superuser:
            
            trackings = TrackingDetails.objects.all()
          
        else:
            trackings = TrackingDetails.objects.filter(user__username = request.user.username)
            
    else:
        trackings = TrackingDetails.objects.filter(user__username = request.user.username)
        
    context = {"trackings":trackings}
    
    return render(request,'tracker_info/view_data.html',context)

@login_required
def download_survey_details(request):
    
    filename = "tracking_sheet_details.xlsx"
    filepath = os.path.join(settings.MEDIA_ROOT,filename)
    
    export_data(filepath)
    
    path = open(filepath,'rb')
    
    response = FileResponse(path,as_attachment=True)
    
    return response
    
# create user 

def register_user(request):
    
    pass 

def activate_user(request):
    
    pass
    
    