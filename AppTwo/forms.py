from django import forms

class LoginForms(forms.Form):
    login = forms.EmailField(label="Nom d'utilisateur", max_length=30, widget=forms.EmailInput)
    pwd = forms.CharField(label="Mot de passe", min_length=4, widget=forms.PasswordInput)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    date_inscrip = forms.DateTimeField(label="Date d'inscription")
