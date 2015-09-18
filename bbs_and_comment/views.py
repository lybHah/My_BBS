# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from app01 import models


class SubComment(View):

    def post(self, request, *args, **kwargs):
        # 获取当前用户
        user = self.request.user
        bbs_user = models.BBS_user.objects.get(user=user)
        comment = self.request.POST.get('comment', '')
        if not user.is_authenticated():
            return HttpResponse("你是怎么post上来的?!", status=403)
        if not comment:
            return HttpResponse("你是怎么post上来的?!", status=403)
        bbs_id = self.request.POST.get('bbs_id', '')
        if not bbs_id:
            return HttpResponse("此文章不存在..", status=403)
        # 保存评论
        the_comment = models.Comment.objects.create(
            content=comment,
            commentator=bbs_user,
            bbs_id=bbs_id,
        )
        # 返回这个评论
        html = "<li style=\"min-height: 100px\">\
                    <div style=\"margin-left: -50px;\">\
                    <img src=\""+unicode(bbs_user.photo)+"\" style=\"width: 50px;height: 50px;\" />\
                    </div>\
                    <div style=\"margin-left: -50px;\">\
                        <label style=\"width: 50px;height: 20px;text-align: center;\">Lv: 1</label>\
                    </div>\
                    <div style=\"position: relative;top: -70px;margin-left: 25px;\">\
                        <h3 style=\"display: inline;\">"+user.username+"</h3>-----------------("+the_comment.date.strftime("%Y-%m-%d %H:%I:%S")+")\
                        <br>\
                        "+the_comment.content+" \
                    </div>\
                    <hr>\
                </li>"
        return HttpResponse(html)

    def get(self, request, *args, **kwargs):
        raise Http404


class DelComment(View):
    def get(self, request, *args, **kwargs):
        comment_id = request.GET.get("comment_id", "")
        if not comment_id:
            return HttpResponse("没有这个评论啊...", status=403)
        # 删除评论
        comment = models.Comment.objects.get(id=comment_id)
        comment.delete()
        return HttpResponse(1)


class SubBbsView(View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        # 获取当前用户
        user = self.request.user
        bbs_user = models.BBS_user.objects.get(user=user)
        bbs_title = self.request.POST.get('bbs_title', '')
        bbs_content = self.request.POST.get('bbs_content', '')
        if not user.is_authenticated():
            return HttpResponse("你是怎么post上来的?!", status=403)
        if not bbs_title:
            return HttpResponse("你是怎么post上来的?!", status=403)
        if not bbs_content:
            return HttpResponse("你是怎么post上来的?!", status=403)
        category_id = self.request.POST.get('category_id','')
        if not category_id:
            return HttpResponse("此板块不存在..", status=403)
        category = models.Category.objects.get(id=category_id)
        # 创建帖子
        new_bbs = models.BBS.objects.create(
            title=bbs_title,
            category=category,
            content=bbs_content,
            author=bbs_user,
        )
        new_bbs_id = new_bbs.id
        return HttpResponse(new_bbs_id)
