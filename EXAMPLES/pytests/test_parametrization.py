#!/usr/bin/env python
import pytest


def triple(x):  # <1>
    return x * 3

test_data = [(5, 15), ('a', 'aaa'), ([True], [True, True, True]), ("FUN", "FUNFUNFUN")]  # <2>

@pytest.mark.parametrize("input,result", test_data)  # <3>
def test_triple(input, result):  # <4>
    print("input {} result {}:".format(input, result))  # <4>
    assert triple(input) == result   # <5>

def add(x, y):
    return x + y


test_data = [(1, 2, 3), (10, 20, 30), (5, 18, 23), (0, 0, 0), (-10, 10, 0)]
@pytest.mark.parametrize("op1,op2,result", test_data)
def test_add(op1, op2, result):
    assert add(op1, op2) == result


if __name__ == "__main__": # if this is the main script, not an imported module
    pytest.main([__file__, '-s'])

