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

from typing import Callable
from itertools import permutations


g1 = [[0, 2, 4, 6], [1, 0, 5, 7], [11, 15, 0, 24], [33, 34, 35, 0]]
g2 = [[0, 1000, 4, 6], [1000, 0, 5, 7], [11, 15, 0, 24], [33, 34, 35, 0]]
negative_graph = [[0, -10, -15, -20], [-10, 0, -35, -25], [-15, -35, 0, -30], [-20, -25, -30, 0]]
names_g1 = {"TLV": [0, 20, 40, 60], "ARIEL": [10, 0, 50, 70], "KFAR-SABA": [330, 340, 350, 0], "KARMIEL": [110, 150, 0, 240]}


def create_city_index_list(graph: dict, start: str) -> tuple:
    count = 0
    start_index = 0
    city_index = {}
    index_list = []
    for k, v in graph.items():
        if k == start_index:
            start_index = count
        city_index[count] = k
        count += 1
        index_list.append(v)
    return start_index, index_list, city_index


def tsp(navigation_graph: [list, dict], start: [int, str], path_flag: bool) -> float:
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

    >>> paths(algorithm=tsp, graph=g1, start=2, path_flag=False)
    55
    >>> paths(algorithm=tsp, graph=g1, start=2, path_flag=True)
    (2, 3, 1, 0)
    >>> paths(algorithm=tsp, graph=names_g1, start="TLV", path_flag=False)
    180
    >>> paths(algorithm=tsp, graph=names_g1, start="TLV", path_flag=True)
    ('TLV', 'KARMIEL', 'KFAR-SABA', 'ARIEL')
    """
    possible_starting_nodes = []
    city_index_result = None
    if isinstance(navigation_graph, dict):
        city_index_result = create_city_index_list(navigation_graph, start)
        start = city_index_result[0]
        navigation_graph = city_index_result[1]
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
        if path_flag and city_index_result is not None:
            result = (city_index_result[2][start],)
            for permutation_index in permutation:
                result += (city_index_result[2][permutation_index], )
        elif path_flag:
            result = (start,) + permutation
        else:
            result = min(result, current_distance)
    return result


def floyd_warshall(graph: list, nodes: tuple, path_flag: bool):
    """"
    Floyd warshalls algorithm that returns all possible shortests paths on a graph


    >>> paths(algorithm=floyd_warshall, graph=g1, start=(1, 3), path_flag=False)
    7
    >>> paths(algorithm=floyd_warshall, graph=g1, start=(1, 2), path_flag=False)
    5
    >>> paths(algorithm=floyd_warshall, graph=g1, start=(1, 1), path_flag=False)
    0
    >>> paths(algorithm=floyd_warshall, graph=g1, start=(3, 1), path_flag=False)
    34
    >>> paths(algorithm=floyd_warshall, graph=g1, start=(2, 1), path_flag=False)
    13
    >>> paths(algorithm=floyd_warshall, graph=g2, start=(2, 1), path_flag=False)
    15
    >>> paths(algorithm=floyd_warshall, graph=g2, start=(1, 2), path_flag=False)
    5
    >>> paths(algorithm=floyd_warshall, graph=g2, start=(1, 2), path_flag=True)
    [1, 2]
    >>> paths(algorithm=floyd_warshall, graph=g2, start=(1, 3), path_flag=True)
    [1, 2, 3]

    """
    path_matrix = graph
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                path_matrix[i][j] = min(path_matrix[i][j], path_matrix[i][k]+path_matrix[k][j])
    if path_flag:
        result = []
        if path_matrix[nodes[0]][nodes[1]] == float('inf'):
            return result
        current = nodes[0]
        for i in range(nodes[0] + 1, nodes[1] + 1):
            next_node = path_matrix[current][nodes[1]]
            if next_node == -1:
                return None
            result.append(current)
            current = i
        if path_matrix[current][nodes[1]] == -1:
            return None
        result.append(nodes[1])
        return result
    return path_matrix[nodes[0]][nodes[1]]


def paths(algorithm: Callable, graph: list, start: [int, None], path_flag: [bool, None]):
    if isinstance(start, tuple):
        return algorithm(graph, start, path_flag)
    else:
        return algorithm(graph, start, path_flag)


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
