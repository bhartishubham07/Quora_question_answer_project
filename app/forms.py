from django import forms


from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'password']
        widgets = {
        'password' : forms.PasswordInput(attrs = {'class':'form-control'}),
        'username':forms.TextInput(attrs = {'class':'form-control'}),
        }
        
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'password']
        widgets = {
        'password' : forms.PasswordInput(attrs = {'class':'form-control'}),
        'username':forms.TextInput(attrs = {'class':'form-control'}),
        }

        

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']
        

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question','description']