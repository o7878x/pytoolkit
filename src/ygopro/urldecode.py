import logging
import typing
from urllib.parse import urlparse, parse_qs

import fire

YGO_SCHEME = 'ygo'
YGO_NETLOC = 'deck'


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

    parts = str.split(part_str, '_')
    for counted_part in parts:
        code_count_pair = str.split(counted_part, '*')

        pair_len = len(code_count_pair)
        if pair_len == 1:
            res.append(counted_part)
        elif pair_len == 2:
            res += [code_count_pair[0]] * int(code_count_pair[1])

    return res


DEFAULT_HEADER = '#created by ...\n'

DEFAULT_SYM = '#'
NO_SYM = '!'

MAIN_HEADER = 'main\n'
EXTRA_HEADER = 'extra\n'
SIDE_HEADER = 'side\n'


def get_deck_str(query_dict: typing.Dict) -> str:
    main_deck_arr = get_code_arr(query_dict['main'][0])
    extra_deck_arr = get_code_arr(query_dict['extra'][0])
    side_deck_arr = get_code_arr(query_dict['side'][0])

    target_str = DEFAULT_HEADER

    target_str += (DEFAULT_SYM + MAIN_HEADER + '\n'.join(main_deck_arr))
    target_str += '\n'

    target_str += (DEFAULT_SYM + EXTRA_HEADER + '\n'.join(extra_deck_arr))
    target_str += '\n'

    target_str += (NO_SYM + SIDE_HEADER + '\n'.join(side_deck_arr))

    return target_str


def save_file(file_name: str, origin_url: str):
    res_str = decode_url(origin_url)

    with open('.'.join([file_name, 'ydk']), 'w') as f:
        f.write(res_str)


if __name__ == '__main__':
    fire.Fire(save_file)
