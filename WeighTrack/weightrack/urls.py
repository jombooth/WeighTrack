from django.conf.urls.defaults import *
from weightrack import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()



urlpatterns = patterns('',

	url(r'^$', views.index, name='index')




    # Example:
    # (r'^WeighTrack/', include('WeighTrack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)
