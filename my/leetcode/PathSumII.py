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
