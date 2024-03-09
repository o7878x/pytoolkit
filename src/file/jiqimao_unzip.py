#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os.path
import time

import file_utils
import zip_utils


def get_target_path(full_path: str) -> str:
    abs_path = os.path.abspath(full_path)
    return os.path.join(abs_path, 'jiqimao_' + time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()) + '_' + str(
        int(time.time() * 1000)))


def main(src_full_path: str, target_full_path: str, pwd: str):
    # check source path exists
    if not file_utils.check_path_exists(src_full_path):
        print('src')
        return

    target_abs_path = get_target_path(target_full_path)
    os.mkdir(target_abs_path)

    print('begin first decompression')
    # iterate and decompress all 7z file in src path
    for tmp_file_name in os.listdir(src_full_path):
        final_full_path = os.path.join(src_full_path, tmp_file_name)
        if not os.path.isfile(final_full_path):
            continue

        if not final_full_path.endswith('.7z'):
            continue

        zip_utils.decompress_7zip(final_full_path, target_abs_path, pwd)

    print('begin second decompression')
    # iterate decompress tmp 7zip files
    for tmp_file_path in os.listdir(target_abs_path):
        final_file_path = os.path.join(target_abs_path, tmp_file_path)
        if not os.path.isfile(final_file_path):
            continue

        if not final_file_path.endswith('.7zz'):
            continue

        # decompress success and remove tmp file
        if zip_utils.decompress_7zip(final_file_path, target_abs_path, pwd):
            os.remove(final_file_path)


if __name__ == '__main__':
    src_path: str = '../test_source'
    target_path: str = '../test_source/'
    password: str = 'jqmcy.top'

    main(src_path, target_path, password)
