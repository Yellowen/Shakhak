# -----------------------------------------------------------------------------
#    Shakhak - Advertisement web application
#    Copyright (C) 2012-2013 Yellowen
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# -----------------------------------------------------------------------------
import os

from django.conf.urls import patterns, include, url
from django.conf import settings
from vakhshour.events.discovery import handler_discovery


handler_discovery()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^auth/', include("daarmaan.client.urls", namespace="daarmaan",
                        app_name="client")),
    url(r'^$', 'shakhak.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^statics/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__),
                                        '../media/statics').replace('\\', '/')}),
)
