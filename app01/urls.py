# -*- coding:utf-8 -*-

from django.conf.urls import include, url, patterns
import views
import api

urlpatterns = patterns('',
                       (r'^$', views.IndexView.as_view()),    # 首页
                       (r'^category/(?P<category_id>\d+)/$', views.CategoryView.as_view()),    # 板块
                       (r'^detail/(?P<bbs_id>\d+)/$', views.BbsDetailView.as_view()),    # 帖子内容
                       (r'^search/$', views.SearchView.as_view()),    # 搜索
                       (r'^login/$', views.LoginAndRegView.as_view(template_name='login.html')),    # 用户登陆
                       (r'^reg/$', views.LoginAndRegView.as_view(template_name='reg.html')),    # 用户注册
                       (r'^personal_center/(?P<user_id>\d+)/$', views.PersonalView.as_view()),    # 个人界面
                       )
