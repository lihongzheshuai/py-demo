'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# author li.hzh 2017-11-29 23:34
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype:
         List[List[int]]
        """
        result = []
        if root is None:
            return result
        curVal = root.val
        subSum = sum - curVal
        if root.left is None and root.right is None and subSum == 0:
            return [[curVal]]
        if root.left is not None:
            left_result = list(self.pathSum(root.left, subSum))
            if len(left_result) != 0:
                for path in left_result:
                    path = list(path)
                    path.insert(0, curVal)
                    result.append(path)
        if root.right is not None:
            right_result = list(self.pathSum(root.right, subSum))
            if len(right_result) != 0:
                for path in right_result:
                    path = list(path)
                    path.insert(0, curVal)
                    result.append(path)
        return result


from my.leetcode.TreeNode import TreeNode

tree = TreeNode(1)
one_left = TreeNode(2)
one_right = TreeNode(2)
tree.left = one_left
tree.right = one_right
one_left.left = TreeNode(3)
one_left.right = TreeNode(3)
one_right.left = TreeNode(3)
one_right.right = TreeNode(3)
print(Solution().pathSum(tree, 6))
