from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Notes

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)        

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = {'title', 'author', 'body'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'user', 'value':'', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = {'title', 'body'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
