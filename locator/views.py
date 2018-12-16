from django.shortcuts import render
import geoip2.database
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
from locator.forms import LocatorForm
from locator.models import Location
from django.contrib.staticfiles.storage import staticfiles_storage


def userloc(request):
    user = request.user
    instance  = Location.objects.get(user=user.id)
    locator_form = LocatorForm()
    ip = "74.136.205.106"
    print(ip)
    p = staticfiles_storage.path('GeoLite2-City.mmdb')
    reader = geoip2.database.Reader(p)
    response = reader.city(str(ip))
    city = response.city.name
    latitude = response.location.latitude
    longitude = response.location.longitude
    if request.method =='POST':
        locator_form =LocatorForm(data=request.POST or None, instance=instance)
        if locator_form.is_valid():
            locator_form.save()
            locator_form = LocatorForm()
            return render(request, 'userloc.html',
                    {'city':city, 'latitude':latitude, 'longitude':longitude, 'locator_form':locator_form, 'next_url': '/userloc',
                'instance':instance, 'username':request.user.username})
    else:
        locator_form = LocatorForm()
        return render(request, 'userloc.html', {'city':city, 'latitude':latitude, 'longitude':longitude, 'locator_form':locator_form, 'next_url':'/userloc', 'instance':instance, 'username': request.user.username})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_client_city(request):
    ip = get_client_ip(request)
    p = staticfiles_storage.path('GeoLite2-City.mmdb')
    reader = geoip2.database.Reader(p)
    response = reader.city(str(ip))
    city = response.city.name
    return str(city)

def get_client_latitude(request):
    '''ip = get_client_ip(request)'''
    ip = '74.136.205.106'
    p = staticfiles_storage.path('GeoLite2-City.mmdb')
    reader = geoip2.database.Reader(p)
    response = reader.city(str(ip))
    latitude = response.location.latitude
    return str(latitude)

def get_client_longitude(request):
    ip = get_client_ip(request)
    p = staticfiles_storage.path('GeoLite2-City.mmdb')
    reader = geoip2.database.Reader(p)
    response = reader.city(str(ip))
    longitude = response.location.longitude
    return str(longitude)
'''
def userloc(request):
    ip = get_client_ip(request)
    ip = '74.136.205.106'
    print(ip)
    reader = geoip2.database.Reader('/home/minty/Documents/Chatango-front-end/GeoLite2-City.mmdb')
    response = reader.city(str(ip))
    city = response.city.name
    latitude = response.location.latitude
    longitude = response.location.longitude
    return HttpResponse("Your IP address is " + str(ip) + "\n" + "Your city is " + str(city) + "/n" + "Your longitude is " + str(longitude) +  "/n" + "Your latitude is" + str(latitude))
'''
def savelocation(request):
    user = request.user
    location = Location.objects.get(user=user.id)
    ip = '74.136.205.106'
    print(ip)
    p = staticfiles_storage.path('GeoLite2-City.mmdb')
    reader = geoip2.database.Reader(p)
    response = reader.city(str(ip))
    city = response.city.name
    latitude = response.location.latitude
    longitude = response.location.longitude
    if request.method == "POST":
        locator_form = Locator_Form(data=request.POST)
        next_url = request.POST.get("next_url", "userloc")
        if locator_form.is_valid():
            savelocation = locator_form.save(commit=False)
            location.user = request.user
            location.save()
            return redirect(next_url)
        else:
            return userloc(request, locator_form, {'city':city, 'latitude':latitude, 'longitude':longitude, 'ip':ip, })
    return redirect('savelocation')

def usermap(request):
    user = request.user
    points = Location.objects.filter(latitude__isnull=False)

    return render(request, 'usermap.html', { 'points':points, 'username':request.user.username})
