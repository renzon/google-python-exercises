from collections import deque


def cat_dog(s):
    """Solution of problem at http://codingbat.com/prob/p164876

    >>> cat_dog('catdog')
    True
    >>> cat_dog('catcat')
    False
    >>> cat_dog('1cat1cadodog')
    True

    """
    last_3_chars = deque(maxlen=3)
    cat = deque('cat')
    dog = deque('dog')
    count = 0
    for c in s:
        last_3_chars.append(c)
        if last_3_chars == cat:
            count += 1
        elif last_3_chars == dog:
            count -= 1
    return count == 0
