# -*- coding:utf-8 -*-

from django.contrib import admin
from app01.models import *

# 定制自己的个性化admin
# 在admin显示BBS的一些字段
class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'view_count', 'created_at', 'updated_at')
# 加一个筛选功能
    list_filter = ('view_count', 'author__user__username',)    # 像author这样的外键要这样用哦
# 加一个搜索功能
    search_fields = ('title', 'ranking', 'author__user__username',)    # 像author这样的外键要这样用哦

admin.site.register(BBS, BBS_admin)
admin.site.register(BBS_user)
admin.site.register(Category)
admin.site.register(Comment)
