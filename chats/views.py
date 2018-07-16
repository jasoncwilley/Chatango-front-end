
from django.contrib.auth.models import User
from chats.models import Spam, Profile
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib import messages
from accounts.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from chats.forms import SpamForm, RegistrationForm, ProfileForm, AuthenticateForm, UserCreateForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticateForm(data=request.POST)
        if login_form.is_valid():
                        # Success
            login(request, login_form.get_user())
            return redirect('/')
        else:
            # Failure
            login_form = AuthenticateForm()
            return render(request, '/users/', {'login_form':login_form})
    return redirect('/')



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
        login_form = login_form or AuthenticationForm()
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
        return Spam.objects.all()[:3]
    except IndexError:
        return ""


@login_required
def users(request,  username="", spam_form=None):
    if username:
        #show the users profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        messages = Spam.objects.filter(user=user.id)

        if username == request.user.username or request.user.profile.follows.filter(username=username):
            return render(request, 'user.html', {'user': user, 'messages': messages, })
        return render(request, 'user.html', {'user': user, 'messages': messages, 'follow': True, })


    users = User.objects.all().annotate(spam_count=Count('spam'))
    messages = map(get_latest, users)
    obj = zip(users, messages)
    spam_form = spam_form or SpamForm()
    return render(request,
                  'profiles.html',
                  {'obj': obj, 'next_url': '/users/',
                   'spam_form': spam_form,
                   'username': request.user.username, })

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
def viewprofile(request, profile_id):
    profile_id == "0"
    userProfile = Profile.objects.get(pk=profile_id)

    return render_to_response('viewprofile.html', {'userProfile':userProfile}, RequestContext(request))
