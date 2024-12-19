from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'input100'}))
    image = forms.ImageField()
