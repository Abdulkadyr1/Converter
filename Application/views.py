from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

import requests
API_KEY = 'a588cb1d0c23b1173e8743d71afbe5db'



# Параметры запроса
url = "http://api.exchangerate.host/convert"


def index(request):
    return render(request, 'Application/index.html')


def result(request):
    params = {
        "access_key": API_KEY,
        "from": "USD",
        "to": "RUB",
        "amount": request.GET['dollar']
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return render(request, "Application/index_result.html", context=data)
    else:
        return HttpResponseNotFound("Не выполнился")