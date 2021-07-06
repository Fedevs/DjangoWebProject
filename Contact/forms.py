from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=30)
    email = forms.EmailField(label="E-mail", required=True)
    message = forms.CharField(label="Message", widget=forms.Textarea)

