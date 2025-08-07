"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # time: O(n^2), space: O(logn)
        def constructRange(top, left, sideLen):
            if sideLen == 1:
                return Node(grid[top][left], True)
            topLeft = constructRange(top, left, sideLen // 2)
            topRight = constructRange(top, left + (sideLen // 2), sideLen // 2)
            botLeft = constructRange(top + (sideLen // 2), left, sideLen // 2)
            botRight = constructRange(top + (sideLen // 2), left + (sideLen // 2), sideLen // 2)
            children = [topLeft, topRight, botLeft, botRight]
            if all(child.isLeaf and child.val == topLeft.val for child in children):
                return Node(topLeft.val, True)
            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        return constructRange(0, 0, len(grid))