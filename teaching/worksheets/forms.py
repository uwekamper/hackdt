from django import forms

class WebHookForm(forms.Form):
    userId = forms.CharField(max_length=200)
    guid = forms.CharField(max_length=1000)
    reason = forms.CharField(max_length=200)