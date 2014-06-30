from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from items.views import *
from profiles.views import *


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rental.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^grapppelli/", include("grappelli.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", index, name="index"),

    # Items
    url(r"^item/(?P<item_id>\d+)/$", view_item, name="view_item"),
    url(r"^item/(?P<item_id>\d+)/reserve/$", reserve_item, name="reserve_item"),

    # Profiles
    url(r"^profile/(?P<user_id>\d+)/$", view_user, name="view_user"),
    url(r"^group/(?P<group_id>\d+)/$", view_group, name="view_group"),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
