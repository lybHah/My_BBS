# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm


class MyUserRegForm(UserCreationForm):

    # error messages
    error_messages = {
        'password_mismatch': "两次密码不相同",
        'password_too_short': "密码长度不能小于6位"
    }
    username = forms.RegexField(
        max_length=20,
        regex=r'^[\w.@_]+$',
        # 错误信息 invalid 表示username不合法的错误信息, required 表示没填的错误信息
        error_messages={
            'invalid': "用户名只能包含字母、数字和\.\@\_",
            'required': "用户名为空",
            'unique': "此用户已存在"
        })
    password1 = forms.CharField(
        label="password",
        max_length=30,
        widget=forms.PasswordInput,
        error_messages={
            'required': "密码为空"
        })
    password2 = forms.CharField(
        label="Password confirmation",
        max_length=30,
        widget=forms.PasswordInput,
        error_messages={
            'required': "确认密码为空"
        })

    # 检查密码长度
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        if password1 and len(password1) < 6:
            raise forms.ValidationError(
                self.error_messages["password_too_short"]
            )
        # 下面这句一定要加上去,是父类方法里面的,不加会报错,继承forms.Form就不用加
        self._validate_unique = True
        return self.cleaned_data


# 其实就是无聊想把框架自带的错误信息都改成中文在发给前端
# 噢,对了,新密码长度也不能少于6位
class MyPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': "旧密码错误,请重新输入",
        'password_mismatch': "两次密码不相同",
        'password_too_short': "新密码长度不能小于6位"
    }

    old_password = forms.CharField(
        label="old_password",
        max_length=30,
        widget=forms.PasswordInput,
        error_messages={
            'required': "请输入旧密码"
        }
    )

    new_password1 = forms.CharField(
        label="new_password",
        max_length=30,
        widget=forms.PasswordInput,
        error_messages={
            'required': "请输入新密码"
        })
    new_password2 = forms.CharField(
        label="Password confirmation",
        max_length=30,
        widget=forms.PasswordInput,
        error_messages={
            'required': "请再次输入新密码"
        })

    # 检查密码长度
    def clean(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if new_password1 and len(new_password1) < 6:
            raise forms.ValidationError(
                self.error_messages["password_too_short"]
            )
        return self.cleaned_data
