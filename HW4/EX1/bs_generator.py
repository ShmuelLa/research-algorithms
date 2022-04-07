lst_tst = [1, 2, 3, 4, 5]
lst_tst2 = [1, 2, 3, 4]


def check_if_contains_list(lst1: list, lst2: list) -> bool:
    """
    checks if lst1 is subset of lst2

    :param lst1: subset to check
    :param lst2: bigger set to check
    :return: true if true false otherwise
    """
    for subset in lst2:
        if all(x in subset for x in lst1):
            return True
    return False


def bounded_subset(lst: list, num: int):
    """"
    A generator that receives a list of numbers and an integers
    Returns an iterator of all the subsets of the list which
    are at least the sum of the received number

    >>> [i for i in bounded_subset((2, 1, 2, 3, 4), 2)]
    Traceback (most recent call last):
     ...
    ValueError: This generator accepts only (list, int) input
    >>> result_tst = [subset for subset in bounded_subset(lst_tst, 2)]
    >>> [1] in result_tst
    True
    >>> [2] in result_tst
    True
    >>> [3] not in result_tst
    True
    >>> result_tst2 = [subset for subset in bounded_subset(lst_tst2, 4)]
    >>> check_if_contains_list([1, 3], result_tst2)
    True
    >>> check_if_contains_list([3], result_tst2)
    True
    >>> check_if_contains_list([5], result_tst2)
    False
    >>> check_if_contains_list([7], result_tst2)
    False
    >>> lst_tst2 = [4, 3, 2, 1]
    >>> result_tst2 = [subset for subset in bounded_subset(lst_tst2, 4)]
    >>> check_if_contains_list([1, 3], result_tst2)
    True
    >>> check_if_contains_list([3], result_tst2)
    True
    >>> check_if_contains_list([5], result_tst2)
    False
    >>> check_if_contains_list([7], result_tst2)
    False

    """

    if not isinstance(lst, list) or not isinstance(num, int):
        raise ValueError("This generator accepts only (list, int) input")
    # Removes numbers that are too big before the heavy iteration to improve complexity
    lst.sort()
    for index in lst:
        if index > num:
            lst.remove(index)
    result = [[]]
    for index in lst:
        tmp_set = [subset + [index] for subset in result]
        # We will add only the relevant subsets that that has the corresponding sum
        result.extend(subs for subs in tmp_set if sum(subs) <= num)
    # After we finish we need to iterate ont more time over the result in order to yield it
    # This part is crucial because we are relying on the list extend/append feature for the creation
    for subset in result:
        yield subset


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
