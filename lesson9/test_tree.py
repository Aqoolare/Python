import sys

sys.path.append('../Lessons/lesson4')

import tree


class TestTree:
    def test_tree_of_two_vertex(self):
        assert tree.bfs([[1], []], 0) == '0, 1'

    def test_tree_with_many_vertices_starting_from_0vertex(self):
        tree1 = [[1, 2], 
                [3, 4, 0],
                [5, 0],
                [6, 7, 8, 1],
                [1],
                [2],
                [3],
                [3],
                [3]]
        assert tree.bfs(tree1, 0) == '0, 1, 2, 3, 4, 5, 6, 7, 8'

    def test_tree_with_many_vertices_starting_from_5vertex(self):
        tree1 = [[1, 2], 
                [3, 4, 0],
                [5, 6, 0],
                [1],
                [7, 8, 1],
                [2],
                [2],
                [4],
                [4]]
        assert tree.bfs(tree1, 5) == '5, 2, 6, 0, 1, 3, 4, 7, 8'

    def test_tree_with_letters(self):
        tree1 = {
            'a':['b','c'],
            'b':['d', 'e', 'a'],
            'c':['f', 'g', 'a'],
            'd':['b'],
            'e':['h','i', 'b'],
            'f':['c'],
            'g':['c'],
            'h':['e'],
            'i':['e']
        }
        assert tree.bfs(tree1, 'f') == 'f, c, g, a, b, d, e, h, i'