# !/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import time
import typing
from urllib.parse import urlparse, parse_qs

import fire

YGO_SCHEME = 'ygo'
YGO_NETLOC = 'deck'

DEFAULT_HEADER = '#created by ...\n'

CARD_SEP_SYM = '_'
CARD_MULTI_SYM = '*'
DEFAULT_SYM = '#'
NO_SYM = '!'

MAIN_HEADER = 'main\n'
EXTRA_HEADER = 'extra\n'
SIDE_HEADER = 'side\n'

DEFAULT_YDK_NAME: str = "default" + "_" + str(int(time.time()))


def decode_url(url: str) -> str:
    res = urlparse(url)
    if not res:
        logging.info('can not parse url')
        return ''

    if res.scheme != YGO_SCHEME or res.netloc != YGO_NETLOC:
        logging.info('it is not a YGO link')
        return ''

    qs = parse_qs(res.query)
    if not qs:
        logging.info('can not parse query')
        return ''

    return get_deck_str(qs)


def get_code_arr(part_str: str) -> typing.List:
    res = []
    if not part_str:
        return res

    parts = str.split(part_str, CARD_SEP_SYM)
    for counted_part in parts:
        code_count_pair = str.split(counted_part, CARD_MULTI_SYM)

        pair_len = len(code_count_pair)
        if pair_len == 1:
            res.append(counted_part)
        elif pair_len == 2:
            res += [code_count_pair[0]] * int(code_count_pair[1])

    return res


def get_target_field_str(target_dict: typing.Dict, field_name: str, index: int = 0) -> str:
    res = ""
    try:
        res = target_dict[field_name][index]
    except KeyError:
        logging.info("key error")
    finally:
        return res


def get_deck_str(query_dict: typing.Dict) -> str:
    main_deck_arr = get_code_arr(get_target_field_str(query_dict, 'main'))
    print(main_deck_arr)
    extra_deck_arr = get_code_arr(get_target_field_str(query_dict, 'extra'))
    side_deck_arr = get_code_arr(get_target_field_str(query_dict, 'side'))

    target_str = DEFAULT_HEADER

    target_str += (DEFAULT_SYM + MAIN_HEADER + '\n'.join(main_deck_arr))
    target_str += '\n'

    target_str += (DEFAULT_SYM + EXTRA_HEADER + '\n'.join(extra_deck_arr))
    target_str += '\n'

    target_str += (NO_SYM + SIDE_HEADER + '\n'.join(side_deck_arr))

    return target_str


def save_file(origin_url: str, file_name: str = DEFAULT_YDK_NAME):
    res_str = decode_url(origin_url)

    with open('.'.join([file_name, 'ydk']), 'w') as f:
        f.write(res_str)


if __name__ == '__main__':
    fire.Fire(save_file)
