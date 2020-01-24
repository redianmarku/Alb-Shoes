from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class Register(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username','name':'username','class': 'form-control' }))
    email = forms.EmailField(label='Enter email', widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-control' }))
    password1 = forms.CharField(label='Vendos nje password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name':'password1','class': 'form-control' }))
    password2 = forms.CharField(label='Konfirmo password', widget=forms.PasswordInput(attrs={'placeholder': 'Konfirmo Password','class': 'form-control' }))
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Ky username ekziston!")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Ky email eshte perdorur me pare!")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Dy format e passowrd nuk jane te njejta!")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user 