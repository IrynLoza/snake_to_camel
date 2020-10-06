"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

    >>> snake_to_camel("hi_balloonicorn_we_ready_to_play")
    'hiBalloonicornWeReadyToPlay'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    phrase = variable_name.split('_')
    result = phrase[:1]

    for word in phrase[1:]:
        word = word.replace(word[0], word[0].upper())
        result.append(word)
    return ''.join(result)    





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
