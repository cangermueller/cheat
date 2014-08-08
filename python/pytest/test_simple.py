#!/usr/bin/env python

import pytest
import sys
import time

def reverse_upper(text):
    return ''.join(reversed(text.upper()))

@pytest.mark.skipif(True, reason='Skip always')
def test_reverse_upper():
    assert reverse_upper('abc') == 'CB'

@pytest.mark.skipif(sys.platform == 'darwin', reason='Platform mismatch')
def test_numbers():
    assert 1 == 3

@pytest.mark.slow
def test_veryslow():
    time.sleep(2)

def add_nums(a, b):
    return a + b

@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (3, 5, 8)])
def test_sum(a, b, c):
    assert add_nums(a, b) == 2 * c

@pytest.mark.xfail
def test_fail():
    assert 1 == 4
