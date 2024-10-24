import unittest

from LargestLevelSum import LargestLevelSum



class TestLargestLevelSum(unittest.TestCase):

    def test_single_node_tree(self):
        root = LargestLevelSum.build_tree_from_level_order([10])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 10)

    def test_full_binary_tree_with_positive_values(self):
        root = LargestLevelSum.build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 22)

    def test_tree_with_all_negative_values(self):
        root = LargestLevelSum.build_tree_from_level_order([-1, -2, -3, -4, -5, -6, -7])
        self.assertEqual(LargestLevelSum.max_level_sum(root), -1)

    def test_tree_with_mixed_positive_and_negative_values(self):
        root = LargestLevelSum.build_tree_from_level_order([1, -2, 3, 4, -5, -6, 7])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 1)

    def test_right_skewed_tree(self):
        root = LargestLevelSum.build_tree_from_level_order([1, -2, None, -3])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 1)

    def test_left_skewed_tree(self):
        root = LargestLevelSum.build_tree_from_level_order([1, 2, None, 3])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 3)

    def test_empty_tree(self):
        root = LargestLevelSum.build_tree_from_level_order([])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 0)

    def test_tree_with_one_child_at_different_levels(self):
        root = LargestLevelSum.build_tree_from_level_order([1, 2, None, 4])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 4)

    def test_perfect_binary_tree_with_all_zeroes(self):
        root = LargestLevelSum.build_tree_from_level_order([0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 0)

    def test_larger_balanced_tree(self):
        root = LargestLevelSum.build_tree_from_level_order([5, 3, 8, 1, 4, 7, 9, 0, 2, 6])
        self.assertEqual(LargestLevelSum.max_level_sum(root), 21)

if __name__ == "__main__":
    unittest.main()
