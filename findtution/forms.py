from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    cemail = forms.EmailField(required=True)
    institute = forms.CharField(required=True)
    message = forms.CharField(required=True,
                              widget=forms.Textarea)




