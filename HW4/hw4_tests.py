from HW4.EX1.bs_generator import bounded_subset
from HW4.EX2.TSP_alg import paths, floyd_warshall, tsp
import unittest




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


class bs_generator_tests(unittest.TestCase):
    """
    Tests for EX1 - bounded subset generator
    """

    # def test_wrong_input(self):
        # tuple_t = (2, 1, 2, 3, 4)
        # # self.assertRaises(ValueError, bounded_subset, tuple_t, 's')
        # try:
        #     for i in bounded_subset(tuple_t, 2):
        #         print(i, end=" ")
        # except ValueError:
        #     self.assertEqual(True,True)
        # else:
        #     self.assertEqual(True, False)

    def test_bs_results(self):
        lst_tst = [1, 2, 3, 4, 5]
        result_tst = [subset for subset in bounded_subset(lst_tst, 2)]
        self.assertTrue([1] in result_tst)
        self.assertTrue([2] in result_tst)
        self.assertTrue([3] not in result_tst)
        lst_tst2 = [1, 2, 3, 4]
        result_tst2 = [subset for subset in bounded_subset(lst_tst2, 4)]
        self.assertTrue(check_if_contains_list([1, 3], result_tst2))
        self.assertTrue(check_if_contains_list([3], result_tst2))
        for i in range(5, 8):
            self.assertFalse(check_if_contains_list([i], result_tst2))
        lst_tst2 = [4, 3, 2, 1]
        result_tst2 = [subset for subset in bounded_subset(lst_tst2, 4)]
        self.assertTrue(check_if_contains_list([1, 3], result_tst2))
        self.assertTrue(check_if_contains_list([3], result_tst2))
        for i in range(5, 8):
            self.assertFalse(check_if_contains_list([i], result_tst2))


class tsp_fw_test(unittest.TestCase):
    """
    EX2 Tests
    """

    # def test_numeric_input(self):
    #     g1 = [[0, 2, 4, 6], [1, 0, 5, 7], [11, 15, 0, 24], [33, 34, 35, 0]]
        # self.assertEqual(55, paths(algorithm=tsp, graph=g1, start=2, path_flag=False))
        # self.assertEqual((2, 3, 1, 0), paths(algorithm=tsp, graph=g1, start=2, path_flag=True))

    # def test_string_input(self):
    #     names_g1 = {"TLV": [0, 20, 40, 60],
    #                 "ARIEL": [10, 0, 50, 70],
    #                 "KFAR-SABA": [330, 340, 350, 0],
    #                 "KARMIEL": [110, 150, 0, 240]}
    #     self.assertEqual(180, paths(algorithm=tsp, graph=names_g1, start="TLV", path_flag=False))
    #     self.assertEqual(('TLV', 'KARMIEL', 'KFAR-SABA', 'ARIEL'),
    #                      paths(algorithm=tsp, graph=names_g1, start="TLV", path_flag=True))

    # def test_floyd_warshall(self):
    #     g1 = [[0, 2, 4, 6], [1, 0, 5, 7], [11, 15, 0, 24], [33, 34, 35, 0]]
    #     self.assertEqual(7, paths(algorithm=floyd_warshall, graph=g1, start=(1, 3), path_flag=False))
    #     self.assertEqual([1, 1, 7], paths(algorithm=floyd_warshall, graph=g1, start=(1, 3), path_flag=True))


if __name__ == "__main__":
    unittest.main()
