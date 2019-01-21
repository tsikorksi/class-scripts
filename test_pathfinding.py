from pathfinding import a_star
from pathfinding import dijkstra

import unittest


class DijkstraTest(unittest.TestCase):
    def test_basic(self):
        """
        the basic case tested for, plus bonus variations
        """
        graph = {
            'a': {'b': 1, 'c': 2},
            'b': {'a': 1, 'c': 2, 'd': 3},
            'c': {'a': 2, 'b': 2, 'd': 1},
            'd': {'b': 3, 'c': 1}
        }
        self.assertEqual(('acd', 3), dijkstra(graph, 'a', 'd'))
        self.assertEqual(('dca', 3), dijkstra(graph, 'd', 'a'))
        self.assertEqual(('bd', 3), dijkstra(graph, 'b', 'd'))

    def test_simple(self):
        """
        the graph for one of the div exercises, in two variations
        """
        graph = {
            'a': {'b': 5, 'd': 3, 'c': 3},
            'b': {'a': 5, 'f': 2},
            'c': {'a': 3, 'f': 3, 'e': 3},
            'd': {'a': 3, 'e': 2},
            'e': {'d': 2, 'c': 3},
            'f': {'b': 2, 'c': 3}
        }
        self.assertEqual(('ade', 5), dijkstra(graph, 'a', 'e'))
        self.assertEqual(('acf', 6), dijkstra(graph, 'a', 'f'))

    def test_weird_cases(self):
        graph = {
            'a': {}
        }
        self.assertEqual(('a', 0), dijkstra(graph, 'a', 'a'))
        graph = {
            'a': {'b': 0, 'c': 0},
            'b': {'a': 0, 'c': 0, 'd': 0},
            'c': {'a': 0, 'b': 0, 'd': 0},
            'd': {'b': 0, 'c': 0}
        }
        self.assertEqual(('abd', 0), dijkstra(graph, 'a', 'd'))
        self.assertEqual(('bd', 0), dijkstra(graph, 'b', 'd'))


class AStarTest(unittest.TestCase):

    def test_a_star_basic(self):
        heuristics = {'a': 5, 'b': 3, 'c': 9, 'd': 0}
        graph = {'a': {'b': 1, 'c': 2},
                 'b': {'a': 1, 'c': 2, 'd': 3},
                 'c': {'a': 2, 'b': 2, 'd': 1},
                 'd': {'b': 3, 'c': 1}
                 }
        start, end = 'a', 'd'
        self.assertEqual(('abd', 4), a_star(graph, heuristics, start, end))

    def test_a_star_advanced(self):
        graph = {
            'a': {'b': 5, 'd': 3, 'c': 3},
            'b': {'a': 5, 'f': 2},
            'c': {'a': 3, 'f': 3, 'e': 3},
            'd': {'a': 3, 'e': 2},
            'e': {'d': 2, 'c': 3},
            'f': {'b': 2, 'c': 3}
        }
        heuristics = {'a': 5, 'b': 30, 'c': 5, 'd': 15, 'e': 10, 'f': 0}
        start, end = 'a', 'f'
        self.assertEqual(('acf', 6), a_star(graph, heuristics, start, end))
