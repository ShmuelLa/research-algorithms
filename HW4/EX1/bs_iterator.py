def bounded_subset(lst: list, num: int):
    if not isinstance(lst, list) or not isinstance(num, int):
        raise ValueError("This generator accepts only (list, int) input")
    for index in lst:
        if index > num:
            lst.remove(index)
    lst.sort()
    result = [[]]
    for index in lst:
        tmp_set = [subset + [index] for subset in result]
        result.extend(tmp_set)
    for subset in result:
        if sum(subset) <= num:
            yield subset


if __name__ == "__main__":
    for i in bounded_subset([1, 2, 3, 4, 5, 6, 7, 8], 4):
        print(i, end=" ")
