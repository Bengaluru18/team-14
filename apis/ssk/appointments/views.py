from django.shortcuts import render
import requests
import json
from datetime import datetime, timedelta
from dateutil.parser import parse


# Create your views here.
def medi_view(request, id):
    resp = requests.get("http://127.0.0.1:8000/api/v1/medi/{}".format(id))
    medi_json =  resp.json() # json.loads(resp.decode('utf-8'))
    print(medi_json)
    if request.method == "GET":
        date = datetime.today()
    else:
        date = parse(request.POST.get["date"])
    params = {
        "medi__id": id,
        "start_time__gte": date,
        "end_time__lte": date + timedelta(days=1),

    }
    resp = requests.get("http://127.0.0.1:8000/api/v1/mediavailability/", params=params)
    return resp.json()
