from django import forms


class UserBioForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(label='Input age')
    bio = forms.CharField(label='Input your biography', widget=forms.Textarea)

