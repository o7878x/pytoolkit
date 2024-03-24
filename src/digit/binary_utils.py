#!/usr/bin/env python
# -*- coding:utf-8 -*-

def is_odd_integer(x: int) -> bool:
    return x & 1 == 1


def is_power_of_two(x: int) -> bool:
    return x & (x - 1) == 0


def low_bit(x: int) -> int:
    return x & (-x)


def mod_m(x: int, m: int) -> int:
    return x & (m - 1)


if __name__ == '__main__':
    assert is_odd_integer(1)
    assert not is_odd_integer(2)
    assert is_odd_integer(3)

    assert is_power_of_two(2)
    assert not is_power_of_two(3)

    assert low_bit(1) == 1
    assert low_bit(2) == 2

    assert mod_m(5, 4) == 1
