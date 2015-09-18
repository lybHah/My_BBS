# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,所以修改str类的title方法就可以实现.
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


# 性别
SEX = {
    0: u'男',
    1: u'女',
    2: u'其他',
}

SEXUAL_ORIENTATION = {
    0: u'同性恋',
    1: u'异性恋',
    2: u'双性恋',
    3: u'跨种族',
}


class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True)
    category = models.ForeignKey('Category')
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField(default=0)
    total_comment = models.IntegerField(default=0)
    is_top = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'帖子'
        ordering = ['-created_at']    # 按照创建时间倒序的顺序在后台排序存储
        app_label = string_with_title('app01', u'论坛管理')

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    administrator = models.ForeignKey('BBS_user')

    class Meta:
        verbose_name_plural = verbose_name = u'板块'
        app_label = string_with_title('app01', u'论坛管理')

    def __unicode__(self):
        return self.name


class BBS_user(models.Model):
    user = models.OneToOneField(User)
    sex = models.IntegerField(default=2, choices=SEX.items())    # 0是男，1是女，2是其他>_<
    sexual_orientation = models.IntegerField(default=1, choices=SEXUAL_ORIENTATION.items())    # 0是同，1是异，2是双性恋，3是跨种族
    phone_num = models.IntegerField(default=10086, blank=True, null=True)    # 可以为空
    signature = models.CharField(max_length=50, default='This gay is too lazy to leave anything here.')
    # 下面这个路径需要根据不同项目修改
    photo = models.ImageField(upload_to="/project/bbs_pro/statics/upload_imgs/", default="/static/images/shit.png")

    class Meta:
        verbose_name_plural = verbose_name = u'用户'
        app_label = string_with_title('app01', u'论坛管理')

    def __unicode__(self):
        return self.user.username


class Comment(models.Model):
    content = models.TextField()
    commentator = models.ForeignKey('BBS_user')
    bbs_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'评论'
        ordering = ['-date']    # 按照创建时间倒序的顺序在后台排序存储
        app_label = string_with_title('app01', u'论坛管理')

    def __unicode__(self):
        return self.content
