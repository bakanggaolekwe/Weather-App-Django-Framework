from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

# Create your views here.
def home(request):
    if request.method =='POST':
        location = request.POST['city']
        # sending an api call
        api = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+location+'&APPID=7fc6c20db75625b03bdbe6eb4c954a6d').read()
        # converting the json data gotten from the api call to a dictionary
        list_of_data = json.loads(api)
    
        context = {
            "country_code": list_of_data['sys']['country'],
            "description": list_of_data['weather'][0]['description'],
            "temperature": list_of_data['main']['temp'],
            "pressure": list_of_data['main']['pressure'],
            "humidity": list_of_data['main']['humidity'],
            'icon':list_of_data["weather"][0]['icon'],
            'city':list_of_data['name'],

        }
    else:
        context={}
    return render(request,'core/index.html',context)