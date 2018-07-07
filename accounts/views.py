from django.shortcuts import render, redirect
from  accounts.forms import RegistrationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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


@login_required
def profile(request, profile_id):
    if profile_id == "0":
        if request.user.is_authenticated:
            userProfile = UserProfile.objects.get(pk=profile_id)
    else:
        userProfile = UserProfile.objects.get(pk=profile_id)

    return render_to_response('blog/profile.html', {'userProfile':userProfile}, RequestContext(request))


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
