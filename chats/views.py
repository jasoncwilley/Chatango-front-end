
from django.contrib.auth.models import User
from chats.models import Spam, Profile, PrivateSpam
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib import messages
from accounts.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from chats.forms import PrivateSpamForm, SpamForm, RegistrationForm, ProfileForm, AuthenticateForm, UserCreateForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist






@login_required
def submit(request):
    if request.method == "POST":
        spam_form = SpamForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if spam_form.is_valid():
            submit = spam_form.save(commit=False)
            spam.user = request.user
            spam.save()
            return redirect(next_url)
        else:
            return public(request, spam_form)
    return redirect('/')


def index(request, login_form=None, reg_form=None):
    # User is logged in
    if request.user.is_authenticated():
        messages = Spam.objects.order_by('-timestamp')
        spam_form = SpamForm()
        user = request.user
        my_spam = Spam.objects.filter(user=user.id)
        friends_spam = Spam.objects.filter(user__profile__in=user.profile.follows.all)
        spam = my_spam | friends_spam



        return render(request, 'buddies.html',
                  {'spam_form': spam_form, 'user': user, 'messages':messages,
                   'spam': spam,
                       'next_url': '/', })
    else:
        # User is not logged in
        login_form = login_form or AuthenticateForm()
        reg_form = reg_form or UserCreateForm()

        return render(request,
            'home.html',
            {'login_form': login_form, 'reg_form': reg_form, })


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


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('user.html')
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
        return Spam.objects.all()[:3]
    except IndexError:
        return ""

@login_required
def updateprofile(request):
    if request.method=='POST':
        reg_form = RegistrationForm(data=request.POST)
        if profile_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect('/')
    else:
        reg_form = RegistrationForm()

    args = {'reg_form':reg_form }
    return render(request, 'register.html', args)
@login_required
def users(request,  username="", spam_form=None):
    if username:
        #show the users profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        messages = Spam.objects.filter(user=user.id)
        users = User.objects.all().annotate(spam_count=Count('spam'))
        profile_form = ProfileForm()
        if username == request.user.username or request.user.profile.follows.filter(username=username):
            try:
                profile = request.user.profile
            except Profile.DoesNotExist:
                raise Http404
                profile = Profile(user=request.user)

            if request.method == "POST":
                profile_form = ProfileForm(request.POST, instance=profile)
                if profile_form.is_valid():
                    profile_form.save()
                    profile_form = ProfileForm()
                    return render(request, 'user.html', {'user':user, 'messages': messages, 'profile_form': profile_form})
            return render(request, 'user.html', {'user': user, 'messages': messages, 'profile_form': profile_form,})
        return render(request, 'user.html', {'user': user, 'messages': messages, 'follow': True, })


    users = User.objects.all().annotate(spam_count=Count('spam'))
    messages = map(get_latest, users)
    obj = zip(users, messages)
    spam_form = spam_form or SpamForm()
    return render(request,
                  'profiles.html',
                  {'obj': obj, 'next_url': '/users/',
                   'spam_form': spam_form,
                   'username': request.user.username })

@login_required
def follow(request):
    if request.method == "POST":
        follow_id = request.POST.get('follow', False)
        if follow_id:
            try:
                user = User.objects.get(username=follow_id)
                request.user.profile.follows.add(user.profile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')

@login_required
def public(request, spam_form=None):
    messages = Spam.objects.order_by('-timestamp')
    spam_form = spam_form or SpamForm()
    if request.method =='POST':
        spam_form =SpamForm(data=request.POST)
        if spam_form.is_valid():
            spam = spam_form.save(commit=False)
            spam.user = request.user
            spam.save()
            return render(request, 'public.html',
                    {'spam_form':spam_form, 'next_url': '/public',
                    'messages':messages, 'username':request.user.username})
    return render(request, 'public.html',
{'spam_form':spam_form, 'next_url':'/public', 'messages':messages, 'username': request.user.username})

@login_required
def followers(request, username='', form=None):
    followers = request.user.profile.follows.all
    return render(request, 'followers.html',
                {'followers':followers, 'username':request.user.username})


@login_required
def following(request, username='', form=None):
    followings = request.user.profile.followed_by.all
    return render(request, 'following.html',
    {'followings':followings, 'username': request.user.username})

@login_required
def private(request, username='', form=None):
    form = form or PrivateSpamForm()
    username = request.user.username
    messages = PrivateSpam.objects.filter(user = request.user)
    if request.method == "POST":
        form = PrivateSpamForm(data=request.POST)
        if form.is_valid():
            ch = form.cleaned_data.get('reciever')
            privatespam = form.save(commit=False)
            privatespam.user = request.user
            privatespam.save()
            form = PrivateSpamForm()
            return render(request, 'private.html',
                    {'form':form, 'next_url': '/followers', 'messages': messages,
                     'username':request.user.username})
    form = PrivateSpamForm()
    return render(request, 'private.html',
    {'form':form, 'next_url':'/private',  'messages': messages, 'username': request.user.username})

@login_required
def send_private(request, form=None):
    form = form or PrivateSpamForm()
    user=request.user
    messages = PrivateSpam.objects.filter(user_id=user.id)
    if request.method == "POST":
        form = PrivateSpamForm(data=request.POST)
        if form.is_valid():
            ch = form.cleaned_data.get('reciever')
            privatespam = form.save(commit=False)
            privatespam.user = request.user
            privatespam.save()
            form =PrivateSpamForm()
            return render(request, 'send.html',
                    {'form':form, 'next_url': '/followers', 'messages': messages,
                     'username':request.user.username})
    form = PrivateSpamForm()
    return render(request, 'send.html',
    {'form':form, 'next_url':'/send',  'messages': messages, 'username': request.user.username})
@login_required
def check_private(request):
    user=request.user
    messages = user.reciever.all()
    return render(request,"check.html",{'messages':messages})

@login_required
def friends(request, username='', form=None):
    form = form or PrivateSpamForm()
    user = request.user
    followings = request.user.profile.follows.all
    followers = request.user.profile.followed_by.all
    if request.method == "POST":
        form = PrivateSpamForm(data=request.POST)
        if form.is_valid():
            ch = form.cleaned_data.get('reciever')
            privatespam = form.save(commit=False)
            privatespam.user = request.user
            privatespam.save()
            return render(request, 'friends.html',
                    {'form':form, 'next_url': '/followers',
                    'followings':followings, 'followers':followers, 'username':request.user.username})
    return render(request, 'friends.html',
    {'form':form, 'next_url':'/friends', 'followings':followings, 'followers':followers, 'username': request.user.username})

def unfollow(request, username=""):
    user = request.user
    username = request.user.username
    follows = user.profile.follows.filter(username=username)
    profile = Profile.objects.all

    username = request.user.username
    followed_by = Profile.objects.get(user__username=username)
    user = request.user
    if request.method=="POST":
        Profile.objects.get(follows)
        follows.remove(followed_by)
        follows_count = follows.all().count()
        user.save()
        followed_by.remove(user)
        otheruser.follow_by_count = otheruser.followed_by.all().count()
        otheruser.save()
        return render(request, 'following.html',
                {'username':request.user.username })
    else:
        return HttpResponse("unfollow did not save")
