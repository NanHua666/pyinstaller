#-----------------------------------------------------------------------------
# Copyright (c) 2005-2015, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


import os
import pytest

from PyInstaller.compat import is_win
from PyInstaller.utils.tests import importorskip, xfail_py2


# Directory with data for some tests.
_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')



def test_relative_import(pyi_builder):
    pyi_builder.test_script('pyi_import_relative.py')


def test_relative_import2(pyi_builder):
    pyi_builder.test_script('pyi_import_relative2.py')


def test_relative_import3(pyi_builder):
    pyi_builder.test_script('pyi_import_relative3.py')


def test_ctypes_CDLL_c(pyi_builder):
    pyi_builder.test_script('pyi_ctypes_CDLL_c.py')
