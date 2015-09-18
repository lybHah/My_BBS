# -*- coding:utf-8 -*-

from django.conf.urls import include, url, patterns
from bbs_user import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       (r'^usercontrol/(?P<slug>\w+)/$', views.UserControlView.as_view()),
                       )
