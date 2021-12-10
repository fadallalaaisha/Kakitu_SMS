from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    number = forms.CharField(label= 'Code', help_text= "Enter the verification code")
    class Meta:
        model = Code
        fields = ('number',)
        