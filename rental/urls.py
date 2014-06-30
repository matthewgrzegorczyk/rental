from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from items import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rental.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^grapppelli/", include("grappelli.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", views.index, name="index"),
    url(r"^item/(?P<item_id>\d+)/$", views.view_item, name="view_item"),
    url(r"^item/(?P<item_id>\d+)/reserve/$", views.reserve_item, name="reserve_item")

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
