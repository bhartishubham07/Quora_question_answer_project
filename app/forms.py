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
        fields = ['title']
        
        labels={
            'title': 'Write Question :',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'})
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question','description']
        
        labels={
            'question': 'Select Question',
            'description': 'Write Answer Here :',
        }
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':20}),
            'question':forms.Select(attrs={'class':'form-control'})
        }