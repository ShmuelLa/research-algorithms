class List(list):
    """
    HW2 - EX3

    Multidimensional list object, changed core elements to fit the list.
    Most of the methods used are based on the super class.
    """

    def __init__(self, matrix: list):
        """
        Initializes the objects and check is the input is correct and working properly

        :param matrix: a multidimensional list, needs to receive a list withing a list with equal dimensions
        """
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
        """
        Returns a specific index within the object

        :param args: a multidimensional index [x,y,z]
        :return: the object in the current index
        """
        if isinstance(args[0], int):
            return self.matrix.__getitem__(args[0])
        elif len(args[0]) == 2:
            return self.matrix.__getitem__(args[0][0]).__getitem__(args[0][1])
        else:
            return self.matrix.__getitem__(args[0][0]).__getitem__(args[0][1]).__getitem__(args[0][2])

    def append(self, *args):
        if not isinstance(args[0], List) and not isinstance(args[0], list):
            raise SyntaxError("Can only receive list or List as object type for appending")
        return self.matrix.append(args[0].matrix)

    def remove(self, *args):
        if not isinstance(args[0], List) and not isinstance(args[0], list):
            raise SyntaxError("Can only receive list or List as object type for removing")
        return self.matrix.remove(args[0])

    def __eq__(self, other):
        if isinstance(other, list):
            return self.matrix == other
        return self.matrix == other.matrix

    def __len__(self):
        return self.first_dimension_length
        
    def __str__(self):
        return self.matrix.__str__()


if __name__ == "__main__":
    """
    Used for realtime development printing, actual tests are in hw2_tests.py module   
    """
    lst = [[[1, 2, 3], [2, 3, 1]],
           [[1, 2, 3], [2, 3, 1]]]
    lst2 = [[[1, 2, 3], [2, 3]], [[1, 2, 3]]]  # raises error
    list1 = List(lst)
    print(list1[0, 1, 1])
