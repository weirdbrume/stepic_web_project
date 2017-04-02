from django import forms
from qa.models import Question, Answer
from django.shortcuts import get_object_or_404


class AskForm(forms.Form):
    title = forms.CharField(max_length='255')
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError(u'Field "Title" should not be empty!')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(u'Field "Text" should not be empty!')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(u'Field "Text" should not be empty')
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Wrong question number')

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
