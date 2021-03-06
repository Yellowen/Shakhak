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

from django.conf.urls import patterns, url

from advertises.dashboard.views import AdvertiseList, AdvertiseForm


urlpatterns = patterns('',
    url(r'^$', 'advertises.dashboard.views.index', name='dashboard-index'),
    url(r'^advertises/$', AdvertiseList.as_view(), name='advertise-list'),
    url(r'^advertises/new/$', AdvertiseForm.as_view(), name='advertise-form'),

)
