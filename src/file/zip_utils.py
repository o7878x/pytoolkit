#!/usr/bin/env python
# -*- coding:utf-8 -*-

import py7zr

import file_utils


def decompress_7zip(full_file_path: str, target_file_path: str, pwd: str = '') -> bool:
    if not file_utils.check_path_exists(full_file_path):
        print('check full file path not exists')
        return False

    if not file_utils.check_path_exists(target_file_path):
        print('check target path exists')
        return False

    with py7zr.SevenZipFile(full_file_path, mode='r', password=pwd) as file_obj:
        file_obj.extractall(target_file_path)
    return True


if __name__ == '__main__':
    pass
