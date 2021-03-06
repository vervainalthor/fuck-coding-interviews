# coding: utf-8
import random
import unittest

from data_structures.b_trees.b_plus_tree import BPlusTree


class BPlusTreeTest(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(ValueError):
            BPlusTree(order=2)

        self.b_plus_tree = BPlusTree(order=5)
        self.size = random.randint(1, 1000)
        self.keys = random.sample(range(1000), k=self.size)
        for i in self.keys:
            self.b_plus_tree.insert(i, f'{i}')

    def test__len__(self):
        self.assertEqual(len(self.b_plus_tree), self.size)

    def test__iter__(self):
        self.assertEqual(list(self.b_plus_tree), sorted(self.keys))

    def test_get(self):
        for key in self.keys:
            self.assertEqual(self.b_plus_tree.get(key), f'{key}')

        with self.assertRaises(KeyError):
            self.b_plus_tree.get(-1)

    def test_insert(self):
        b_plus_tree = BPlusTree(order=3)

        b_plus_tree.insert(86, '86')
        self.assertEqual(b_plus_tree.root.keys, [86])
        self.assertEqual(b_plus_tree.root.values, ['86'])
        self.assertEqual(list(b_plus_tree), [86])

        with self.assertRaises(KeyError):
            b_plus_tree.insert(86, '86')

        b_plus_tree.insert(99, '99')
        self.assertEqual(b_plus_tree.root.keys, [86, 99])
        self.assertEqual(b_plus_tree.root.values, ['86', '99'])
        self.assertEqual(list(b_plus_tree), [86, 99])

        b_plus_tree.insert(5, '5')
        self.assertEqual(b_plus_tree.root.keys, [86])
        self.assertEqual([leaf.keys for leaf in b_plus_tree.root.values], [[5], [86, 99]])
        self.assertEqual([leaf.values for leaf in b_plus_tree.root.values], [['5'], ['86', '99']])
        self.assertEqual(list(b_plus_tree), [5, 86, 99])

        b_plus_tree.insert(17, '17')
        self.assertEqual(b_plus_tree.root.keys, [86])
        self.assertEqual([leaf.keys for leaf in b_plus_tree.root.values], [[5, 17], [86, 99]])
        self.assertEqual([leaf.values for leaf in b_plus_tree.root.values], [['5', '17'], ['86', '99']])
        self.assertEqual(list(b_plus_tree), [5, 17, 86, 99])

        b_plus_tree.insert(24, '24')
        self.assertEqual(b_plus_tree.root.keys, [17, 86])
        self.assertEqual(b_plus_tree.root.values[0].keys, [5])
        self.assertEqual(b_plus_tree.root.values[1].keys, [17, 24])
        self.assertEqual(b_plus_tree.root.values[2].keys, [86, 99])
        self.assertEqual(list(b_plus_tree), [5, 17, 24, 86, 99])

        b_plus_tree.insert(53, '53')
        self.assertEqual(b_plus_tree.root.keys, [24])
        self.assertEqual(b_plus_tree.root.values[0].keys, [17])
        self.assertEqual(b_plus_tree.root.values[1].keys, [86])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[0].values], [[5], [17]])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[1].values], [[24, 53], [86, 99]])
        self.assertEqual(list(b_plus_tree), [5, 17, 24, 53, 86, 99])

        b_plus_tree.insert(31, '31')
        self.assertEqual(b_plus_tree.root.keys, [24])
        self.assertEqual(b_plus_tree.root.values[0].keys, [17])
        self.assertEqual(b_plus_tree.root.values[1].keys, [31, 86])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[0].values], [[5], [17]])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[1].values], [[24], [31, 53], [86, 99]])
        self.assertEqual(list(b_plus_tree), [5, 17, 24, 31, 53, 86, 99])

        with self.assertRaises(KeyError):
            b_plus_tree.insert(86, '86')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(99, '99')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(5, '5')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(17, '17')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(24, '24')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(53, '53')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(31, '31')


if __name__ == '__main__':
    unittest.main()
