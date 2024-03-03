import pandas as pd
import os
from django.conf import settings
from .models import TrackingDetails
def lookup_hhid(hhid):
    
    file = os.path.join(settings.MEDIA_ROOT,'tracking.xlsx')
    
    data = pd.read_excel(file)
    print(data.columns)
    lookup_data = data[data["hhid"]==hhid]
    
    return lookup_data.to_dict('records')

def export_data(filename):
    
    export_df = pd.DataFrame(list(TrackingDetails.objects.all().values()))
    print(export_df["attempt1_date"])
    
    export_df["attempt1_date"] = export_df["attempt1_date"].apply(lambda x: x.strftime("%d-%m-%Y %H:%M:%S") if not pd.isnull(x) else str(x))
    export_df["attempt2_date"] = export_df["attempt2_date"].apply(lambda x: x.strftime("%d-%m-%Y %H:%M:%S") if not pd.isnull(x) else str(x))
    export_df["attempt3_date"] = export_df["attempt3_date"].apply(lambda x: x.strftime("%d-%m-%Y %H:%M:%S") if not pd.isnull(x) else str(x))
    export_df["if_rr_surveyed_date"] = export_df["if_rr_surveyed_date"].apply(lambda x: x.strftime("%d-%m-%Y %H:%M:%S") if not pd.isnull(x) else str(x))
    export_df["last_updated"] = export_df["last_updated"].apply(lambda x: x.strftime("%d-%m-%Y %H:%M:%S") if not pd.isnull(x) else str(x))
    
    export_df.to_excel(filename,index=False)
    
def load_users():
    
    df = pd.read_excel(r'C:\Users\user\Music\survey_tracker\tracker\tracker_info\users.xlsx',sheet_name='KAP F-D Final Team')
    
    return df
    

    
    
    
    
    
    


