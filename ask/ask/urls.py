"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa.views import test, new_questions, popular, question, ask, answer, signup

urlpatterns = [
    url(r'^$', new_questions, name='new_questions'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', signup, name='signup'),
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
    url(r'^answer/', answer, name='answer'),
    url(r'^ask/', ask, name='ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
