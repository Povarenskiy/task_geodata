from django import forms


class DocxForm(forms.Form):
    cadastral_number = forms.CharField(label='Кадастровый номер', required=False)
    title = forms.CharField(label='Название', required=False)
    text = forms.CharField(label='Текст', widget=forms.Textarea, required=False)

