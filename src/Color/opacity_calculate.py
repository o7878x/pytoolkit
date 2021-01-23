_MIN_TWO_DIGIT_HEX: int = 0x00
_MAX_TWO_DIGIT_HEX: int = 0xFF


def calculate_hex_digit(num: int) -> str:
    if num < _MIN_TWO_DIGIT_HEX or num > _MAX_TWO_DIGIT_HEX:
        raise RuntimeError('num is invalid and can not convert hex')
    return hex(num)[2:].upper()


def calculate_opacity(percent_float: float) -> str:
    if percent_float < 0.0 or percent_float > 1.0:
        raise RuntimeError('percent is invalid')
    two_digit_hex = round(_MAX_TWO_DIGIT_HEX * percent_float)
    return calculate_hex_digit(two_digit_hex)


if __name__ == '__main__':
    print(calculate_hex_digit(26))

    print(calculate_opacity(0))
    print(calculate_opacity(0.13))
    print(calculate_opacity(0.27))