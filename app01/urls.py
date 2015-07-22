from django.conf.urls import include, url, patterns
import views

urlpatterns = patterns('',
                       (r'^$', views.index),
                       (r'^detail/(\d+)/$', views.bbs_detail),
)
