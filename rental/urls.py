from django.conf.urls import patterns, include, url

from django.contrib import admin

from items import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rental.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grapppelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
)
