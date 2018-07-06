
from django.contrib.auth.models import User
from chats.models import Spam, UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from chats.forms import SpamForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'chats/profile.html')
    else:
        form = UserCreationForm()

        args = {'form':form }
        return render(request, 'register.html', args)






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


def updateprofile(request):
    new_user = UserProfile(fname = 'jimbo', lname = 'johnson', username = 'jimbo', phone = '859-873-9577', dateofbirth = '1980-05-20', email = 'jim@bo.com', datecreated = '2010-05-05')
    new_user.save()
    return render(request, 'updateprofile.html')
