
from django.contrib.auth.models import User
from chats.models import Spam, Profile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from chats.forms import SpamForm, RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    if request.method =='POST':
        form = SpamForm(request.POST)
        if form.is_valid():
            home = form.save(commit=False)
            home.user = request.user
            home.save()
            content =  form.cleaned_data['content']
            subject = form.cleaned_data['subject']
            form.save()
            return HttpResponseRedirect('recent')
    else:
        form = SpamForm()
    args = {'form':form}
    return      render(request, 'home.html', args)

def recent(request):
    messages=Spam.objects.all()
    return render(request, 'recent', {'messages':messages})

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('recent')
    else:
        form = RegistrationForm()

    args = {'form':form }
    return render(request, 'register.html', args)





@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.username)




def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', {'action': "Display all Profiles", 'profiles': profiles})

def get_latest(user):
    try:
        return user.spam.set.order_by('id').reverse()[0]
    except IndexError:
        return ""

def users(request,  username="", spam_form=None):
    messages = Spam.objects.all().order_by('-timestamp')
    if username:
        #show the users profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        usermessages = Spam.objects.filter(user=user.id)
        if username == request.user.username or request.user.profile.follows.filter(username=username):
            return render(request, 'user.html', {'user': user, 'usermessages': usermessages, })
        return render(request, 'user.html', {'user': user, 'usermessages': usermessages, 'follow': True, })
    users = User.objects.all().annotate(spam_count=Count('messages'))
    usermessages = map(get_latest, users)
    obj = zip(users, usermessages)
    spam_form = spam_form or SpamForm()
    return render(request,
                  'profiles.html',
                  {'obj': obj, 'next_url': '/users/',
                   'spam_form': spam_form,
                   'username': request.user.username, })



def profile(request, pk):
    profile = User.objects.get(id=pk)
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
