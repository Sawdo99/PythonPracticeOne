def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]


s = 'hello'
# s[start:stop:step]
s[1:4]  # 'ell'
s[:3]  # 'hel'
s[2:]  # 'llo'
s[::2]  # 'hlo'
s[::-1]  # 'olleh'