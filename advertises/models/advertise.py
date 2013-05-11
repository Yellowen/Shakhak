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

from django.utils.translation import ugettext as _
from djamo import Document, Collection
from djamo.serializers import DjangoUser, List, EmbeddedDocument, String
from djamo.utils import six

from .log import Log


class Advertise (Document):
    """
    This class represent an advertise
    """
    fields = {
        "user": DjangoUser(),
        "logs": List(EmbeddedDocument(Log), required=True),
        "title": String(required=True, max_length=256),
    }

    log_msg = ""

    def log(self, msg):
        if not msg:
            raise ValueError("'msg' should not be empty")

        self.log_msg = six.u(msg)

    def save(self, *args, **kwargs):
        if "logs" not in self:
            self.logs = [Log(msg=self.log_msg or _("Advertise saved"))]
        else:
            self.logs.append(Log(msg=self.log_msg or _("Advertise saved")))

        super(Advertise, self).save(*args, **kwargs)


class Advertises (Collection):
    document = Advertise

    class Meta:
        app_label = "advertises"
