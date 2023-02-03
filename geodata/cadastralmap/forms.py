from django import forms


class CadastralForm(forms.Form):
    cadastral_number = forms.CharField(max_length=100, label="")