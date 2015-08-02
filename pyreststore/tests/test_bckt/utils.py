# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

from bckt.models import Bckt
from django.contrib.auth.models import User
import json


def create_bckt(title='Test by BcktTest.create_bckt()',
                contents='Default contents of this bucket',
                jsonBckt=None,
                user=None):
    '''
    Create a Bckt instance based on the contents of the string jsonBckt, which
    must be a json formatted string containing the required Bckt fields.

    If jsonBckt is None, a Bckt is createt with a title and some content.
    '''
    if not jsonBckt:
        return Bckt.objects.create(title=title,
                                   language='text',
                                   code=contents,
                                   owner=user)
    b = json.loads(jsonBckt)
    return Bckt.objects.create(title=b['title'],
                               language=b['language'],
                               code=b['code'],
                               owner=user)
