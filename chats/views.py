from django.shortcuts import render
from django.contrib.auth.models import User
from chats.models import Spam, UserProfile
from django.shortcuts import render

def index(request):
    new_message = Spam(

    sender = "admin",
    content = "this is my first view post",
    timestamp = "2010-02-02")
    new_message.save()
    return render(request, 'index.html', {'action':'Save datas of model'})


def profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles.html', {'action': "Display all UserProfiles", 'profiles': profiles})

def profile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    messages = Spam.objects.all()

    context = {
		"profile": profile,
		"messages": messages,
		}
    return render(request, 'profile_detail.html', context)
