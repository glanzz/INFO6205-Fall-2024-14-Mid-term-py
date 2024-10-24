from collections import deque

"""
 Example:
     Given the following binary tree:
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
    
     Level 0: 1                    -> sum = 1
     Level 1: 2 + 3                -> sum = 5
     Level 2: 4 + 5 + 6 + 7        -> sum = 22
    
     The maximum level sum is 22.
    
     You need to traverse each level of the tree, calculate the sum of the values
     at that level, and keep track of the maximum sum encountered.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LargestLevelSum:
    @staticmethod
    def max_level_sum(root: TreeNode) -> int:
        """
        Finds the maximum level sum in a binary tree.

        :param root: The root of the binary tree
        :return: The largest sum of any level in the tree
        """
        # Implement the logic to find the maximum level sum of the given binary tree.
        if not root:
            return 0
        queue = deque([(root, 0)])
        
        
        levels_sums = {}
        while queue:
            # Logic to process nodes at the current level will go here.
            node, level = queue.pop()
            if not node:
                continue
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
            levels_sums[level] =  levels_sums.get(level, 0) + node.val

        
        return max([val for val in levels_sums.values()])

    @staticmethod
    def build_tree_from_level_order(level_order: list) -> TreeNode:
        """
        Builds a binary tree from a level-order traversal array.

        :param level_order: The level-order traversal array
        :return: The root of the constructed binary tree
        """
        if not level_order or level_order[0] is None:
            return None

        root = TreeNode(level_order[0])
        queue = deque([root])
        i = 1

        while i < len(level_order):
            current_node = queue.popleft()

            if i < len(level_order) and level_order[i] is not None:
                current_node.left = TreeNode(level_order[i])
                queue.append(current_node.left)
            i += 1

            if i < len(level_order) and level_order[i] is not None:
                current_node.right = TreeNode(level_order[i])
                queue.append(current_node.right)
            i += 1

        return root


