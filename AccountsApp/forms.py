from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class StudentRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name' : 'usernane',
            'type': 'text',
            'id' : 'usernane',
            'class' : 'form-input',
            'placeholder' : 'Oladiran sarah',
            'maxlenght' : '16',
            'minlenght' : '6'
        })
         
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name' : 'email',
            'type': 'email',
            'id' : 'email',
            'class' : 'form-input',
            'placeholder' : 'soladiran25@gmail.com'
        })
        self.fields["matric_number"].widget.attrs.update({
            'required': '',
            'name' : 'matric_number',
            'id' : 'matric_number',
            'type': 'matric_number',
            'class' : 'form-input',
            'placeholder' : 'matric number',
            'maxlenght' : '9',
            'minlenght' : '9'
        })
        
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name' : 'password1',
            'id' : 'password1',
            'type': 'password',
            'class' : 'form-input',
            'placeholder' : 'password',
            'maxlenght' : '22',
            'minlenght' : '8'
        })
          
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'name' : 'password2',
            'id' : 'password2',
            'type': 'password',
            'class' : 'form-input',
            'placeholder' : 'password',
            'maxlenght' : '22',
            'minlenght' : '8'
        })
       

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'matric_number', 'password1', 'password2']

class InstructorRegistrationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["username"].widget.attrs.update({
                'required': '',
                'name' : 'usernane',
                'type': 'text',
                'id' : 'usernane',
                'class' : 'form-input',
                'placeholder' : 'Mrs. Usman Mariam',
                'maxlenght' : '16',
                'minlenght' : '6'
            })
            
            self.fields["email"].widget.attrs.update({
                'required': '',
                'name' : 'email',
                'type': 'email',
                'id' : 'email',
                'class' : 'form-input',
                'placeholder' : 'edu-tech400l@gmail.com'
            })
         
            self.fields["password1"].widget.attrs.update({
                'required': '',
                'name' : 'password1',
                'id' : 'password1',
                'type': 'password',
                'class' : 'form-input',
                'placeholder' : 'password',
                'maxlenght' : '22',
                'minlenght' : '8'
            })
            
            self.fields["password2"].widget.attrs.update({
                'required': '',
                'name' : 'password2',
                'id' : 'password2',
                'type': 'password',
                'class' : 'form-input',
                'placeholder' : 'password',
                'maxlenght' : '22',
                'minlenght' : '8'
            })
        
    class Meta:
            model = CustomUser
            fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class InstructorLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    matric_number = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Matric Number'}))
