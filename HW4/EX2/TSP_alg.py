"""
TSP Algorithm

Author: Shmuel Lavian

Sources used for information:
https://en.wikipedia.org/wiki/Travelling_salesman_problem
https://blog.routific.com/travelling-salesman-problem#:~:text=To%20solve%20the%20TSP%20using,this%20is%20the%20optimal%20solution.&text=This%20method%20breaks%20a%20problem,solved%20into%20several%20sub%2Dproblems.
https://blog.routific.com/travelling-salesman-problem#:~:text=The%20Travelling%20Salesman%20Problem%20(TSP,computer%20science%20and%20operations%20research.
https://www.baeldung.com/cs/tsp-dynamic-programming#:~:text=Dynamic%20Programming%20Approach%20for%20Solving%20TSP&text=If%20the%20number%20of%20cities,distance%20as%20a%20base%20case.&text=%2C%20then%20we'll%20calculate%20the,remaining%20cities%20is%20calculated%20recursively.
https://content.iospress.com/articles/fundamenta-informaticae/fi1760#:~:text=Abstract,(i.e.%2C%20Hamiltonian%20cycles).
"""

from typing import Callable, Any
from itertools import permutations


def tsp(navigation_graph: list, start: int, path_flag: bool) -> float:
    """
    Solves the TSP shortest distance problem in the brute force algorithm
    We will calculate all possible permutations for a path with itertools permutations
    and return it's distance if it's the shortest available

    The main core of this algorithm is to calculate all possible Hamiltonian Cycles possible on the graph

    :param path_flag: A flag to return the full path if True or just the distance if False
    :param navigation_graph: A two dimensional matrix representing the possible nodes and paths the agent needs to pass
    The graph should be a distance matrix graph as described here:
    https://en.wikipedia.org/wiki/Distance_matrix#:~:text=In%20general%2C%20a%20distance%20matrix,paths%20joining%20the%20two%20nodes.

    :param start: The index of the starting point for the agent, has to be a point on the graph
    :return: The shortest path value
    """
    possible_starting_nodes = []
    for node in range(len(navigation_graph)):
        if node != start:
            possible_starting_nodes.append(node)
    result = float('inf')
    for permutation in permutations(possible_starting_nodes):
        current_distance = 0
        tmp = start
        for permutation_node in permutation:
            current_distance += navigation_graph[tmp][permutation_node]
            tmp = permutation_node
        current_distance += navigation_graph[tmp][start]
        if path_flag:
            result = (start,) + permutation
        else:
            result = min(result, current_distance)
    return result


def floyd_warshall(graph: list, start: int):
    paths = graph
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                paths[i][j] = min(paths[i][j], paths[i][k]+paths[k][j])
    return paths


def paths(algorithm: Callable, graph: list, start: int, path_flag: bool):
    return algorithm(graph, start, path_flag)


if __name__ == "__main__":
    g1 = [[0, 2, 4, 6], [1, 0, 5, 7], [11, 15, 0, 24], [33, 34, 35, 0]]
    names_g1 = {"TLV": [0, 20, 40, 60],
                "ARIEL": [10, 0, 50, 70],
                "KFAR-SABA": [330, 340, 350, 0],
                "KARMIEL": [110, 150, 0, 240]}
    print(paths(algorithm=tsp, graph=g1, start=2, path_flag=False))
    print(paths(algorithm=tsp, graph=g1, start=2, path_flag=True))
    # print(tsp_min_dist(g1, 2))
    # print(tsp_min_dist(g1, 3))
    # print(tsp_min_path(g1, 0))
    # print(tsp_min_path(g1, 2))
    # print(tsp_min_path(g1, 3))
    # print(floyd_warshall(g1, 0))



# def partition(algorithm: Callable, numbins: int, items: list, outputtype: out.OutputType=out.Partition):
#     if isinstance(items, dict):  # items is a dict mapping an item to its value.
#         item_names = items.keys()
#         valueof = items.__getitem__
#     else:  # items is a list
#         item_names = items
#         valueof = lambda item: item
#     bins = outputtype.create_empty_bins(numbins)
#     bins.set_valueof(valueof)
#     algorithm(bins, item_names, valueof)
#     return outputtype.extract_output_from_bins(bins)
#
#
# def roundrobin(bins: Bins, item_names: list, valueof: Callable[[Any], float] = lambda x:x):
#     """
#     Partition the given items using the round-robin algorithm.
#     >>> roundrobin(BinsKeepingContents(2), item_names=[1,2,3,3,5,9,9]).bins
#     [[9, 5, 3, 1], [9, 3, 2]]
#     >>> roundrobin(BinsKeepingContents(3), item_names=[1,2,3,3,5,9,9]).bins
#     [[9, 3, 1], [9, 3], [5, 2]]
#     """
#     ibin = 0
#     for item in sorted(item_names, key=valueof, reverse=True):
#         bins.add_item_to_bin(item, ibin)
#         ibin = (ibin+1) % bins.num
#     return bins
#
#
# def greedy(bins: Bins, item_names: list, valueof: Callable[[Any], float] = lambda x:x):
#     """
#     Partition the given items using the greedy number partitioning algorithm.
#
#     >>> greedy(BinsKeepingContents(2), item_names=[1,2,3,3,5,9,9]).bins
#     [[9, 5, 2], [9, 3, 3, 1]]
#     >>> greedy(BinsKeepingContents(3), item_names=[1,2,3,3,5,9,9]).bins
#     [[9, 2], [9, 1], [5, 3, 3]]
#     """
#     for item in sorted(item_names, key=valueof, reverse=True):
#         index_of_least_full_bin = min(range(bins.num), key=lambda i: bins.sums[i])
#         bins.add_item_to_bin(item, index_of_least_full_bin)
#     return bins



