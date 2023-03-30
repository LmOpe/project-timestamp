from datetime import datetime
from django.http import JsonResponse
import time as tm

# Create your views here.
def time(request, date = None):
    try:
        if date != None:
            unix = datetime.utcfromtimestamp(date / 1000.0)
            date_time = unix.strftime("%a, %d %b %Y %H:%M:%S GMT")
            result = {'unix': date, 'utc': date_time}
            return JsonResponse(result)
        else:
            unix = int(tm.time())
            print(unix)
            date = datetime.utcfromtimestamp(unix)
            print(date)
            date_time = date.strftime("%a, %d %b %Y %H:%M:%S GMT")
            print(date_time)
            result = {'unix': unix, 'utc': date_time}
            return JsonResponse(result)

    except:
            return JsonResponse({"error": "Invalid date"})