from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


class AskForm(forms.Form):
    title = forms.CharField(max_length='255')
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError(u'Field "title" should not be empty!')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(u'Field "text" should not be empty!')
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
            raise forms.ValidationError(u'Field "text" should not be empty')
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Wrong question number')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError(u'Field "username" should not be empty')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError(u'Field "email" should not be empty')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise forms.ValidationError(u'Field "password" should not be empty')
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        authenticated_user = authenticate(**self.cleaned_data)
        return authenticated_user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError(u'Field "username" should not be empty')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise forms.ValidationError(u'Field "password" should not be empty')
        return password

    def save(self):
        authenticated_user = authenticate(**self.cleaned_data)
        return authenticated_user
