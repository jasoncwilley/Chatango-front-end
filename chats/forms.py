
from django.contrib.auth.models import User
from django import forms
from chats.models import UserProfile, Spam
from datetime import datetime



class SpamForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'contentText'})),


    def is_valid(self):
        form = super(SpamForm, self).is_valid()
        for f in self.errors.iterkeys():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error contentText'})
        return form

    class Meta:
        model = Spam
        exclude = ('user',)
