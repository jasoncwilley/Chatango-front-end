
from django.contrib.auth.forms import User
from django import forms
from chats.models import Spam, Profile
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class SpamForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'contentText'})),
    subject = forms.CharField(max_length=50)

    class Meta:
        model = Spam
        exclude = ('user','timestamp',)


class ProfileForm(forms.ModelForm):
    fname = forms.CharField(max_length=50, required=False)
    lname = forms.CharField(max_length=50, required=False)
    username = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = (
            'fname',
            'lname',
            'username',
            'phone',
            'email'
        )
