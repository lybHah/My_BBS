# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.contrib import auth
from app01 import models
import json
from bbs_user.forms import MyUserRegForm
from bbs_user.forms import MyPasswordChangeForm


class UserControlView(View):
    def post(self, request, *args, **kwargs):
        # 获取用户需要进行什么操作
        operation = self.kwargs.get('slug', '')

        if operation == 'login':
            return self.login(request)
        elif operation == 'reg':
            return self.reg(request)
        elif operation == 'change_password':
            return self.change_password(request)
        elif operation == 'personal_info':
            return self.personal_info(request)
        raise PermissionDenied

    def get(self, request, *args, **kwargs):
        # 获取用户需要进行什么操作
        operation = self.kwargs.get('slug', '')
        if operation == 'logout':
            return self.logout(request)
        raise PermissionDenied

    def login(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        errors = []
        if user is not None:
            auth.login(request, user)
        else:
            errors.append("用户名或密码不正确")
        my_json = {"errors": errors}
        return HttpResponse(json.dumps(my_json), content_type='application/json')

    def logout(self, request):
        if request.user.is_authenticated():
            auth.logout(request)
            return HttpResponseRedirect("/")
        else:
            raise PermissionDenied

    def reg(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password1', '')
        errors = []
        form = MyUserRegForm(request.POST)
        if form.is_valid():
            # 参考django.contrib.auth.forms.UserCreationForm 的 save() 方法
            form.save()
            # 顺便也登陆了
            user = auth.authenticate(username=username, password=password)
            models.BBS_user.objects.create(user=user)    # 关联到BBS_user
            auth.login(request, user)
        else:
            # 如果表单不正确, 把错误信息保存到errors列表里面
            for k, v in form.errors.items():
                errors.append(v.as_text())
        my_json = {"errors": errors}
        return HttpResponse(json.dumps(my_json), content_type='application/json')

    def change_password(self, request):
        if not request.user.is_authenticated():
            raise PermissionDenied
        errors = []
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 登出
            auth.logout(request)
        else:
            # 如果表单不正确, 把错误信息保存到errors列表里面
            for k, v in form.errors.items():
                errors.append(v.as_text())
        my_json = {"errors": errors}
        return HttpResponse(json.dumps(my_json), content_type='application/json')

    def personal_info(self, request):
        if not request.user.is_authenticated():
            raise PermissionDenied
        bbs_user = models.BBS_user.objects.get(user=request.user)
        errors = []
        signature = request.POST.get('signature', '')
        sex = request.POST.get('sex', '0')
        sexual_orientation = request.POST.get('sexual_orientation', '0')
        phone_num = request.POST.get('phone_num', '')
        if len(signature) > 50:
            errors.append("个性签名长度不能超过25字")
            my_json = {"errors": errors}
            return HttpResponse(json.dumps(my_json), content_type='application/json')
        if phone_num == '':
            phone_num = None
        else:
            if len(phone_num) > 13 or not phone_num.isdigit():
                errors.append("手机号码错误")
                my_json = {"errors": errors}
                return HttpResponse(json.dumps(my_json), content_type='application/json')
        bbs_user.signature = signature
        bbs_user.sex = sex
        bbs_user.sexual_orientation = sexual_orientation
        bbs_user.phone_num = phone_num
        bbs_user.save()
        my_json = {"errors": errors}
        return HttpResponse(json.dumps(my_json), content_type='application/json')


# https://docs.djangoproject.com/en/1.8/ref/forms/validation/#validating-fields-with-clean
# https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#django.forms.ModelForm
