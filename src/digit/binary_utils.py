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


def fast_power(x: int, n: int) -> int:
    # ref: https://zhuanlan.zhihu.com/p/95902286
    res = 1
    while n > 0:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res


def is_same_sign_except_zero(x: int, y: int) -> int:
    return (x ^ y) >= 0


if __name__ == '__main__':
    assert is_odd_integer(1)
    assert not is_odd_integer(2)
    assert is_odd_integer(3)

    assert is_power_of_two(2)
    assert not is_power_of_two(3)

    assert low_bit(1) == 1
    assert low_bit(2) == 2

    assert mod_m(5, 4) == 1

    assert fast_power(2, 10) == 1024

    assert not is_same_sign_except_zero(10, -9)
    assert is_same_sign_except_zero(10, 10)
    assert is_same_sign_except_zero(-10, -10)
