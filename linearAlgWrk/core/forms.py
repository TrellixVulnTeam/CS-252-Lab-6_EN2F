from djano import forms

from .models import Input

class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ('input_str')
