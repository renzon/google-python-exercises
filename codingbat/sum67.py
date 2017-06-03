from functools import partial


def sum67(nums):
    """Solution to the problem described in http://codingbat.com/prob/p108886

    Ex:
    >>> sum67([1, 2, 2])
    5
    >>> sum67([1, 2, 2, 6, 99, 99, 7])
    5
    >>> sum67([1, 1, 6, 7, 2])
    4

    :param nums: list
    :return: int
    """
    sum = 0
    between_6_and_7 = False

    for n in nums:
        if n == 6:
            between_6_and_7 = True
        if not between_6_and_7:
            sum += n
        elif n == 7:
            between_6_and_7 = False

    return sum


def sum67(nums):
    """Solution to the problem described in http://codingbat.com/prob/p108886

    Ex:
    >>> sum67([1, 2, 2])
    5
    >>> sum67([1, 2, 2, 6, 99, 99, 7])
    5
    >>> sum67([1, 1, 6, 7, 2])
    4

    :param nums: list
    :return: int
    """

    def between(n, not_between):
        if n == 7:
            return 0, not_between
        return 0, between

    def not_between(n):
        if n == 6:
            return 0, between
        return n, not_between

    between = partial(between, not_between=not_between)

    current_state = not_between
    sum = 0
    for n in nums:
        n_or_zero, current_state = current_state(n)
        sum += n_or_zero
    return sum
