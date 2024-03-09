#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path
import time
from typing import Tuple


def get_time_millis_str_now() -> str:
    return str(int(time.time() * 1000))


def get_time_nanos_str_now() -> str:
    return str(int(time.time_ns()))


def check_path_exists(file_path: str) -> bool:
    return os.path.exists(file_path)


def is_path_valid(file_path: str) -> bool:
    if not file_path:
        return False
    return os.path.isdir(file_path)


def is_file_valid(file_path: str) -> bool:
    if not file_path:
        return False
    return os.path.isfile(file_path)


def get_split_parts(full_file_path: str) -> Tuple[str, str, str]:
    if not is_file_valid(full_file_path):
        raise RuntimeError('full file path is not valid')

    file_path, file_name = os.path.split(full_file_path)
    file_name_prefix, file_name_suffix = os.path.splitext(file_name)
    return file_path, file_name_prefix, file_name_suffix


def get_file_name_with_timestamp(full_file_path: str, divider: str = '_') -> str:
    abs_path = os.path.abspath(full_file_path)
    file_path, file_name_prefix, file_name_suffix = get_split_parts(abs_path)
    new_file_name = file_name_prefix + divider + get_time_millis_str_now() + file_name_suffix
    return os.path.join(file_path, new_file_name)


if __name__ == '__main__':
    assert not is_file_valid('')
    assert is_file_valid(__file__)
    assert len(get_split_parts(__file__)) == 3

    print(get_time_millis_str_now())
    print(get_time_nanos_str_now())
    print(get_file_name_with_timestamp(__file__))
