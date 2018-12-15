
from django.contrib.auth.forms import User
from django import forms
from chats.models import Spam, Profile, PrivateSpam
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1',
                  'password2']
        model = User

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

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
    content = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Enter Messege 140 Characters Max ','class': 'messageText', 'size':'50'}))
    subject = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Insert Subject Here'}))

    class Meta:
        model = Spam
        exclude = ('user','timestamp',)



class PrivateSpamForm(forms.ModelForm):
    username = forms.ModelChoiceField(queryset=User.objects.all(),
                              empty_label="(Select Private Message Recipent)")
    subject = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Insert Subject Here'}))
    content = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Enter Messege 140 Characters Max ','class': 'messageText', 'size':'50'}))

    class Meta:
        model = PrivateSpam
        exclude = ('user','timestamp',)

    def save(self, commit=True):
        user = super(PrivateSpamForm, self).save(commit=False)
        user.follows = self.cleaned_data['username']
        user.subject = self.cleaned_data['subject']
        user.content = self.cleaned_data['content']
        if commit:
            user.save()
        return user

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
    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
