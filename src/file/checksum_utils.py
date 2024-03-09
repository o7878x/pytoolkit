#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import os.path


def get_file_md5(file_name: str) -> str:
    if not file_name:
        raise RuntimeError('file name is empty')

    if not os.path.isfile(file_name):
        raise RuntimeError('file name is invalid')

    with open(file_name, 'rb') as f:
        file_content = f.read()
        md5_value = hashlib.md5(file_content).hexdigest()
    return md5_value


def check_md5_valid(file_name: str, expected_md5_value: str) -> bool:
    if not expected_md5_value:
        raise RuntimeError('expected md5 value is empty')

    return get_file_md5(file_name) == expected_md5_value


if __name__ == '__main__':
    print(get_file_md5(__file__))
