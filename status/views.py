from django.http import JsonResponse
import os
from datetime import datetime

def status_view(request):
    status_value = os.getenv('MY_WEB_APP_STATUS', None)
    if status_value:
        response = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': status_value
        }
    else:
        response = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'MY_WEB_APP_STATUS is not set'
        }
    return JsonResponse(response)