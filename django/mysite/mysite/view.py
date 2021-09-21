import json
from django.http import HttpResponse
import requests

def func(reuest):
    response = requests.get('http://127.0.0.1:3000/test/get_data')
    return HttpResponse(response)
