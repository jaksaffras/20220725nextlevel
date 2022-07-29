#!/usr/bin/env python

def test_two_plus_two_equals_four():  # <1>
    assert 2 + 2 == 4   #  <2>

def test_none_is_false():
    print("HI MOM!", end="")
    assert bool(None) is False
