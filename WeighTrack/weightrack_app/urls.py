from django.conf.urls import patterns, url
from weightrack_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^about/$', views.user_about, name='about'),
        url(r'^myWeighTrack/$', views.user_devices, name='mydevices'),
        url(r'^devReg/$', views.user_device_reg, name='device_reg'),
        #change views.t to views.req for actual day
        url(r'^req/.*$', views.t, name='request'),

        )