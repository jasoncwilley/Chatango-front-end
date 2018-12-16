
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

    def save(self, commit=True):
        user = super(SpamForm, self).save(commit=False)
        user.subject = self.cleaned_data['subject']
        user.content = self.cleaned_data['content']
        if commit:
            user.save()
        return user

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
    bio = forms.CharField(label='Bio', widget=forms.TextInput(attrs={'style': 'width:209px' ,'class': 'form-text'}))
    username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'style': 'width:209px' ,'class': 'form-text'}))
    fname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'style': 'width:209px' ,'class': 'form-text'}))
    lnamne = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'style': 'width:209px', 'class': 'form-text'}))
    address1 = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'style': 'width:430px', 'class': 'form-text'}))
    address2 = forms.CharField(max_length=35, required=False, widget=forms.TextInput(attrs={'style': 'width:430px', 'class': 'form-text'}))
    city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'style': 'width:200px', 'class': 'form-text'}))
    state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'style': 'width:90px', 'class': 'form-text'}))
    zipcode = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'style': 'width:114px', 'class': 'form-text'}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'style': 'width:210px', 'class': 'form-text'}))
    phone1 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'style': 'width:45px', 'class':'form-text'}))
    phone2 = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'style': 'width:45px', 'class':'form-text'}))
    phone3 = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'style': 'width:92px', 'class':'form-text'}))
    date_created = forms.DateTimeField(
        widget=forms.HiddenInput(),
        required=False
    )
    last_connection = forms.DateTimeField(
        widget=forms.HiddenInput(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['fname'].widget.attrs['placeholder'] = 'First Name'
        self.fields['lname'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['bio'].widget.attrs['placeholder'] = 'Use this space to introduce and tell other Chatango users about yourself.'
        self.fields['address1'].widget.attrs['placeholder'] = 'Street Address'
        self.fields['address2'].widget.attrs['placeholder'] = 'Apt or Suite'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'ZipCode'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['phone1'].widget.attrs['placeholder'] = '859'
        self.fields['phone2'].widget.attrs['placeholder'] = '873'
        self.fields['phone3'].widget.attrs['placeholder'] = '5555'

    class Meta:
       model = Profile
       fields = ['username', 'bio', 'fname', 'lname', 'address1', 'address2', 'city', 'state', 'zipcode', 'email', 'phone1', 'phone2', 'phone3']
       excluded = ['date_created', 'last_connection']

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        user.email = self.cleaned_data['email']
        user.bio = self.cleaned_data['bio']
        user.address1 = self.cleaned_data['address1']
        user.address2 = self.cleaned_data['address2']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.zipcode = self.cleaned_data['zipcode']
        user.phone1 = self.cleaned_data['phone1']
        user.phone2 = self.cleaned_data['phone2']
        user.phone3 = self.cleaned_data['phone3']
        if commit:
            user.save()
        return user
