
from django.contrib.auth.models import User
from chats.models import Spam, Profile
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib import messages
from accounts.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from chats.forms import SpamForm, RegistrationForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

def index(request, login_form=None, reg_form=None):
    # User is logged in
    if request.user.is_authenticated():
        spam_form = SpamForm(request.POST)
        form = login_form or spam_form or reg_form
        if form.is_valid():
            home = spam_form.save(commit=False)
            home.user = request.user
            home.save()
            content =  form.cleaned_data['content']
            subject = form.cleaned_data['subject']
            spam_form.save()
            my_spam = Spam.objects.filter(user=user.id)
            friends_spam = Spam.objects.filter(user__userprofile__in=user.profile.follows.all)
            spam = my_spam| friends_spam

            return render(request,

                      {'spam_form': spam_form, 'user': user,
                       'spam': spam,
                       'next_url': '/', })
        else:
        # User is not logged in
            login_form = login_form or AuthenticationForm()
            reg_form = reg_form or RegistrationForm()

        return render(request,
            'home.html',
            {'login_form': login_form, 'reg_form': reg_form, })






def update(request):
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            username = form.cleaned_data['username']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            form.save()
            return HttpResponseRedirect('latestspam')
    else:
        form = ProfileForm()
    args = {'form':form}
    return      render(request, 'update.html', args)



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
            return HttpResponseRedirect('latestspam')
    else:
        form = SpamForm()
    args = {'form':form}
    return      render(request, 'home.html', args)

def latestspam(request):
    messages=Spam.objects.all()
    return render(request, 'latestspam.html', {'messages':messages})

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('latestspam.html')
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
            user = User.objects.filter(username=username)
        except User.DoesNotExist:
            raise Http404
        usermessages = Spam.objects.filter(user=user)
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

def public(request, form=None):
    messages = Spam.objects.order_by('-timestamp')[:10]

    if request.method =='POST':
        form = SpamForm(request.POST)
        if form.is_valid():
            home = form.save(commit=False)
            home.user = request.user
            home.save()
            content =  form.cleaned_data['content']
            subject = form.cleaned_data['subject']
            form.save()
            return render(request,
                          'public.html',
                          {'form': form, 'next_url': '/public',
                           'messages': messages, 'username': request.user.username})
    else:
        form = SpamForm()

    return render(request, 'public.html', {'form': form, 'next_url': '/public',
                    'messages': messages, 'username': request.user.username})

'''
def profile(request, username=""):
    if username:
        # Show a profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        messages = Spam.objects.filter(user=user.id)
        if username == request.user.username:
            # Self Profile
            return render(request, 'user.html', {'user': user, 'ribbits': ribbits, })
        return render(request, 'user.html', {'user': user, 'messages': messages})
    users = User.objects.all().annotate(ribbit_count=Count('spam'))
    return render(request, 'username': request.user.username, })
'''


@login_required
def viewprofile(request, profile_id):
    profile_id == "0"
    userProfile = Profile.objects.get(pk=profile_id)

    return render_to_response('viewprofile.html', {'userProfile':userProfile}, RequestContext(request))
