# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.http import JsonResponse
import datetime
import models
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView, View
from bbs_pro.settings import PAGE_NUM


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            # 加载导航条内容
            context['category_list'] = models.Category.objects.all()
        except Exception as e:
            return Http404
        return context


class IndexView(BaseMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'bbs_list'
    paginate_by = PAGE_NUM

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        bbs_list = models.BBS.objects.all()
        return bbs_list


class CategoryView(BaseMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'bbs_list'
    paginate_by = PAGE_NUM

    def get_context_data(self, **kwargs):
        category_chosen_id = self.kwargs.get('category_id', '')
        kwargs['category_chosen_id'] = int(category_chosen_id)
        return super(CategoryView, self).get_context_data(**kwargs)

    def get_queryset(self):
        category_chosen_id = self.kwargs.get('category_id', '')
        bbs_list = models.BBS.objects.filter(category__id=category_chosen_id)
        return bbs_list


class BbsDetailView(BaseMixin, DetailView):
    template_name = 'bbs_detail.html'
    pk_url_kwarg = 'bbs_id'    # 修改urls里的匹配标志,默认要使用pk或者slug
    queryset = models.BBS.objects

    def get_context_data(self, **kwargs):
        bbs_id = self.kwargs.get('bbs_id', '')
        kwargs['comment_list'] = models.Comment.objects.filter(bbs_id=bbs_id)
        return super(BbsDetailView, self).get_context_data(**kwargs)


class SearchView(BaseMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'bbs_list'
    paginate_by = PAGE_NUM

    def get_queryset(self):
        keyword = self.request.GET.get('search', '')
        # 使用 Q 在文章标题、内容和摘要里面搜索关键字
        bbs_list = models.BBS.objects.only('title', 'content', 'summary').filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(summary__icontains=keyword)
        )
        return bbs_list


class LoginAndRegView(BaseMixin, TemplateView):
    template_name = 'login.html'


class PersonalView(BaseMixin, DetailView):
    template_name = 'personal_center.html'
    pk_url_kwarg = 'user_id'
    queryset = models.BBS_user.objects
    context_object_name = 'bbs_user'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            html = '''
            用户未登陆
            <br>
            <a href = "/">返回首页</a>
            '''
            return HttpResponse(html)
        else:
            # 返回调用父类的get()方法
            return super(PersonalView, self).get(request, *args, **kwargs)

