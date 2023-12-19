from django import forms


class WebtoonForm(forms.Form):
    location = forms.CharField(max_length=20)
    details = forms.CharField(max_length=200)
    character1name = forms.CharField(max_length=20)
    character1details = forms.CharField(max_length=200)
    character2name = forms.CharField(max_length=20)
    character2details = forms.CharField(max_length=200)
