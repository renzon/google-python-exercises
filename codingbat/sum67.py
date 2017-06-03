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
