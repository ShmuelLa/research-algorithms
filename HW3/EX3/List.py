class List(list):

    def __init__(self, matrix: list) -> object:
        self.first_dimension_length = None
        self.second_dimension_length = None
        if not isinstance(matrix, list):
            raise SyntaxError("Input must be a single or multidimensional list")
        for dimension in matrix:
            if self.first_dimension_length is None:
                self.first_dimension_length = len(dimension)
            elif self.first_dimension_length != len(dimension):
                raise SyntaxError("Each dimension layer size must be equal")
        if isinstance(matrix[0][0], list):
            if self.second_dimension_length is None:
                self.second_dimension_length = len(matrix[0][0])
            for first_d in matrix:
                for second_d in first_d:
                    if len(second_d) != self.second_dimension_length:
                        raise SyntaxError("Each dimension layer size must be equal")
        self.first_dimension_length = len(matrix)
        self.matrix = matrix

    def __getitem__(self, *args):
        if isinstance(args[0], int):
            return self.matrix.__getitem__(args[0])
        elif len(args[0]) == 2:
            return self.matrix.__getitem__(args[0][0]).__getitem__(args[0][1])
        # else -> len(args[0]) == 3
        else:
            return self.matrix.__getitem__(args[0][0]).__getitem__(args[0][1]).__getitem__(args[0][2])

    def __len__(self):
        return self.first_dimension_length
        
    def __str__(self):
        return self.matrix.__str__()


if __name__ == "__main__":
    """
    Used for realtime development printing, actual tests are in hw3_tests.py module   
    """
    lst = [[[1, 2, 3], [2, 3, 1]],
           [[1, 2, 3], [2, 3, 1]]]
    lst2 = [[[1, 2, 3], [2, 3]], [[1, 2, 3]]]  # raises error
    list1 = List(lst)
    # list2 = List(lst2)
    print(list1[0, 1,1])
