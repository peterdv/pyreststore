#!/usr/bin/env python
# -*- coding: utf-8; mode: Python; -*-
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
    """Run the tests defined in this project.

    This file mainly exists to allow ``python setup.py test`` to work.
    :func:`runtests` can be ivoked from any curent working directory.

    Args:

        test_args:
            Arguments passed to the Nose testrunner.

    Usage:

        Run all the tests::

            python pyreststore/tests/runtests.py

        This is equivalent to::

            python pyreststore/tests/runtests.py tests

        Run tests for `PEP 0008`_ conformance of the source code::

            python pyreststore/tests/runtests.py test_pep8

        Only run the tests in the
        :mod:`tests.test_bckt.test_bckt_views` module::

            python pyreststore/tests/runtests.py test_bckt_views
            python pyreststore/tests/runtests.py test_bckt.test_bckt_views
            pyreststore/tests/runtests.py tests.test_bckt.test_bckt_views
            pyreststore/tests/runtests.py test_bckt_views

        all four forms are equivalent,
        the last two requires the file ``runtests.py``
        to be executable by Your user.

    .. _`PEP 0008`: https://www.python.org/dev/peps/pep-0008/
    """
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
