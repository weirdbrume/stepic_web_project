from django import forms
from qa.models import Question


class AskForm(forms.Form):
    title = forms.CharField(max_length='255')
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError('Field "Title" should not be empty!')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError('Field "Text" should not be empty!')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question
