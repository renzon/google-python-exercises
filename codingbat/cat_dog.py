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

    def choose_0_1_or_minus_1(c):
        last_3_chars.append(c)
        if last_3_chars == cat:
            return 1
        elif last_3_chars == dog:
            return -1
        return 0

    return 0 == sum(map(choose_0_1_or_minus_1, s))


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
    dct = dict(cat=1, dog=-1)

    def choose_0_1_or_minus_1(c):
        last_3_chars.append(c)
        return dct.get(''.join(last_3_chars), 0)

    return 0 == sum(map(choose_0_1_or_minus_1, s))


def cat_dog(s):
    """Solution of problem at http://codingbat.com/prob/p164876

    >>> cat_dog('catdog')
    True
    >>> cat_dog('catcat')
    False
    >>> cat_dog('1cat1cadodog')
    True

    """

    cat = deque('cat')
    dog = deque('dog')

    def search(chars):
        last_3_chars = deque(maxlen=3)
        for c in s:
            last_3_chars.append(c)
            if last_3_chars == chars:
                yield chars

    cat_search = search(cat)
    dog_search = search(dog)

    # consume equal number of cats and dogs
    for _ in zip(cat_search, dog_search):
        pass

    def has_next(gen):
        try:
            next(gen)
        except StopIteration:
            return False
        return True

    return not (has_next(cat_search) or has_next(dog_search))
