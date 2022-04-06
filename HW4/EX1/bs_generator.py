def bounded_subset(lst: list, num: int):
    """"
    A generator that receives a list of numbers and an integers
    Returns an iterator of all the subsets of the list which
    are at least the sum of the received number
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
    for i in bounded_subset([1, 2, 3, 4, 5, 6, 7, 8], 4):
        print(i, end=" ")
