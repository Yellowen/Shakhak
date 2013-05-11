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
from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from djamo.utils.views.generic.list import ListView
## from django.contrib.auth.models import User
## from django.views.generic.list import ListView

from advertises.models import Advertises


def index(request):
    return rr("dashboard/index.html",
              {},
              context_instance=RequestContext(request))


class AdvertiseList(ListView):
    collection = Advertises
    #queryset = Advertises().find()
    #model = User
