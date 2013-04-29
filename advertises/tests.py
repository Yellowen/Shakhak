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

from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.auth import get_user_model
from djamo.serializers import String
from djamo.db import client

from advertises.models import Advertise, Advertises


@override_settings(DJAMO={"name": "test_shakhak"})
class AdvertiseTest(TestCase):

    def setUp(self):
        client.drop_database()
        self.user = get_user_model().objects.create_user("user_a",
                                                         "w@w.cc",
                                                         "123456")

    def test_empty_title_save(self):

        ad = Advertise()
        advertises = Advertises()

        self.assertRaisesMessage(String.ValidationError,
                                 "'title' field is required",
                                 advertises.save, ad)

    def test_basic_advertise(self):

        ad = Advertise(title="Advertise 1",
                       user=self.user)

        Advertises().save(ad)

    def test_basic_find(self):

        col = Advertises()

        ad = Advertise(title="Advertise 1",
                       user=self.user)

        col.save(ad)

        ads = col.find()
        adscount = ads.count()
        self.assertNotEqual(adscount, 0, "no document found")
        self.assertTrue(hasattr(ads[0], "logs"), True)
