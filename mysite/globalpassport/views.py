from django.shortcuts import redirect, render
from globalpassport.forms import UserForm
from django.contrib.auth import login, logout, authenticate
from .models import Country
import requests
from django.http.response import HttpResponse


def index(self):
    return HttpResponse("Welcome to your personal Global Travel Passport, Track your Travels!")

# Register
def create_passport(request):
    if request.method == 'POST':
        user_form = UserForm
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm
    return render(request, '/createpassport.html', {user_form : user_form})


def login(request):
    u = request.POST['username']
    p= request.POST['password']
    traveler = authenticate(request, username=u, password=p)
    if traveler is not None:
        login(request, traveler)
        return redirect(myaccount)
    else:
        return 

def my_passport():
    pass
        


def search_country(request, code):
    # code = request.GET.get('code')

    # API Calls
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/"+ code
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "d60eca41e9msh28b55b48d2ff106p197cd0jsn0f40789fc5db"
        }
    response = requests.request("GET", url, headers=headers).json()
    country_data = response['data']
    name = country_data['name']
    capital = country_data['capital']
    code = country_data['code']
    currency_code = country_data['currencyCodes'][0]
    
    
    flag = "flags/"+name+".png"


    # country = Country.objects.create(name=name, capital=capital, code=code, currency_code=currency_code, flag=flag)
    return render(request, 'countrydetails.html', {'name': name, 'capital': capital, 'code': code, 'currency':currency_code, 'flag':flag})


