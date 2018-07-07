
from django.contrib.auth.models import User
from chats.models import Spam, UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from chats.forms import SpamForm, RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            return HttpResponseRedirect('chats/lastestspam.html')
    else:
        form = SpamForm()
    args = {'form':form}
    return      render(request, 'home.html', args)

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('lastestspam,html')
    else:
        form = RegistrationForm()

    args = {'form':form }
    return render(request, 'register.html', args)
'''
def createspam(request):
    if request.method=='POST':
        spam_form = SpamForm(request.POST)
        if spam_form.is_valid():
            spam = spam_form.save(commit=False)
            spam.user = request.user
            spam,save()
            return HttpResponseRedirect('lastestspam.html')
        else:
            spam_form = SpamForm()
            args = {'spam_form':spam_form}

    return HttpResponseRedirect('createspam.html')
'''
def createspam(request):
    if request.POST:
        user = request.POST.get('user', '')
        if 'subject' in request.POST:
            subject = request.POST.get('login', '')
        else:
            error=True
        if 'content' in request.POST:
            content = request.POST.get('content', '')
        else:
            error=True
        if not error:
 # We must get the supervisor
            supervisor = Supervisor.objects.get(id = supervisor_id)
            new_spam = Spam(subject=subject, content=content, user=user)
            new_spam.save()
            return HttpResponse("Developer added")
        else:
            return HttpResponse("An error has occured")
    else:
        listspam= Spam.objects.all()
        return render(request, 'listspam', {'listspam':listspam})




@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.username)




def profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles.html', {'action': "Display all UserProfiles", 'profiles': profiles})

def latestspam(request):
    messages = Spam.objects.all().order_by('-timestamp')
    user = request.user
    page = request.GET.get('page', 4)
    context = {
		"messages": messages,
        "user": user,
		}
    paginator = Paginator(messages, 4)
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)


    return render(request, 'latestspam.html', context)



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
