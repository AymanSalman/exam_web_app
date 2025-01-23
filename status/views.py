from django.http import JsonResponse
import os
from datetime import datetime

def status_view(request):
    status_value = os.getenv('MY_WEB_APP_STATUS', 'MY_WEB_APP_STATUS is not set')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = {
        "Current time now is": current_time,
        "The status of the ENV MY_WEB_APP_STATUS": status_value
    }
    return JsonResponse(response)