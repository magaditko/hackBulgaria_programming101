import unittest

import sys
sys.path.insert(0, '../')

from directed_graph import Graph


class GraphTest(unittest.TestCase):

    def setUp(self):
        self.test_graph = Graph()

    def test_init(self):
        self.assertEqual(self.test_graph.graph, {})

    def test_add_edge_when_nodes_exists(self):
        self.test_graph.graph['a'] = ['b', 'c']
        self.test_graph.add_edge('a', 'b')
        self.assertEqual(self.test_graph.graph['a'], ['b', 'c'])
        self.assertNotEqual(self.test_graph.graph['a'], ['b', 'c', 'b'])

    def test_add_edge_when_nodes_does_not_exitsts(self):
        self.assertEqual(self.test_graph.graph, {})
        self.test_graph.add_edge('m', 'n')
        self.assertEqual(self.test_graph.graph, {'m': ['n']})

    def test_get_neighbours_for_node(self):
        self.test_graph.graph['a'] = ['b', 'c']
        self.test_graph.graph['b'] = ['a', 'c']

        self.assertEqual(self.test_graph.get_neighbours_for_node('a'), ['b', 'c'])

        self.assertEqual(self.test_graph.get_neighbours_for_node('m'), [])

    def test_find_path_loop(self):

        self.test_graph.graph['m'] = ['n', 'b', 'c']
        self.test_graph.graph['n'] = ['o', 'm']
        self.test_graph.graph['o'] = ['p']
        self.test_graph.graph['p'] = ['m', 'z']

        self.assertTrue(self.test_graph.check_if_path_exists('m', 'p'))
        
    def test_find_path(self):
        self.test_graph.graph['a'] = ['b']
        self.test_graph.graph['b'] = ['c', 'd', 'e']
        self.test_graph.graph['d'] = ['f']

        self.assertFalse(self.test_graph.check_if_path_exists('c', 'c'))
        self.assertTrue(self.test_graph.check_if_path_exists('b', 'f'))
        self.assertFalse(self.test_graph.check_if_path_exists('d', 'b'))
        
if __name__ == '__main__':
    unittest.main()
