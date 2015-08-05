#!/usr/bin/env python
# -*- coding: utf-8; mode: Python; -*-

# This file mainly exists to allow python setup.py test to work.
#
# Usage:
#   python setup.py test
#   python pyreststore/tests/runtests.py
#   python pyreststore/tests/runtests.py tests
#   python pyreststore/tests/runtests.py test_pep8
#   python pyreststore/tests/runtests.py test_bckt.test_bckt_views

from __future__ import unicode_literals

import os
import sys
# from django.test.utils import get_runner
from django.conf import settings

# Manipulate sys.path to include modules from this directory
# and from the parent.
# https://docs.python.org/2/tutorial/modules.html#the-module-search-path
here = os.path.abspath(os.path.dirname(__file__))
src = os.path.abspath(os.path.join(here, '..'))
sys.path.insert(0, src)
sys.path.insert(0, here)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pyreststore.settings'


def runtests(*test_args):
    from django_nose import NoseTestSuiteRunner

    if not test_args:
        test_args = ['tests']

    # test_runner = get_runner(settings)
    test_runner = NoseTestSuiteRunner(verbosity=2, interactive=True)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    (options, args) = parser.parse_args()
    runtests(*args)
