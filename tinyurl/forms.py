from django import forms

class TinyURLForm(forms.Form):
    description = forms.CharField(label="Description", max_length=50)
    long_url = forms.CharField(label='Long URL', max_length=500)
