from django.shortcuts import render, redirect
from  accounts.forms import RegistrationForm, AuthenticationForm
from django.http import HttpResponseRedirect

from django.contrib.auth import login

def register(request):

    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('chats/lastestspam.html')
    else:
        form = RegistrationForm()

    args = {'form':form }
    return render(request, 'register.html', args)



def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if form.is_valid():
                        # Success
            user = login_form.get()
            login(request, user)
            return HttpResponseRedirect('chats/lastestspam.html')
    else:
            # Failure
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
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
        return render(request, 'listspam.html', {'listspam':listspam})
