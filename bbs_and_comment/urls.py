# -*- coding:utf-8 -*-

from django.conf.urls import include, url, patterns
from bbs_and_comment import views

urlpatterns = patterns('',
                       (r'^sub_comment/$', views.SubComment.as_view()),    # 添加评论
                       (r'^del_comment/$', views.DelComment.as_view()),    # 删除评论
                       (r'^sub_bbs/$', views.SubBbsView.as_view()),    # 发帖
                       )
