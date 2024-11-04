"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

'''
Create a function which can be called recursively.
Start with the very first grid; 
Iterate over the top row of the grid, after passing a starting position and ending position. 
When the pointer gets over halfway, add it the new node as the next level. 
if there is a change in the grid, set isLeaf to 0, call the function recursively on the length divided in half, in all four quadrants. Keeptrack of that in a variable as isChanging.
If there's no change, set the value of isLeaf to true, and the value to the reocurring value. 
return the Node

'''

class Solution(object):
    def construct(self, grid):
        maxLeft = 0
        maxRight = len(grid[0])
        maxTop = 0
        maxBottom = len(grid)

        def checkGrid (left,right,top,bottom):
            node = Node()
            firstVal = grid[top][left]
            isLeaf = True
            for i in range(left,right):
                for j in range(top,bottom):
                    if firstVal !=grid[j][i]:
                        isLeaf = False

            print(isLeaf,top,bottom,firstVal)
            
            if isLeaf ==False:
                
                halfwayAcross = (left +right)//2
                halfwayUp = (top+bottom)//2
                print(left,right,top,bottom,halfwayUp,halfwayAcross)
                node.topLeft = checkGrid(left,halfwayAcross,top,halfwayUp)
                node.topRight = checkGrid(halfwayAcross,right,top,halfwayUp)
                node.bottomLeft = checkGrid(left,halfwayAcross,halfwayUp,bottom)
                node.bottomRight = checkGrid(halfwayAcross,right,halfwayUp,bottom)
                node.val = firstVal
                node.isLeaf = 0
                print(node.isLeaf,node.val)
            else:
                node.val= firstVal
                node.isLeaf = 1
                print(node.isLeaf,node.val)
            return node


        if len(grid) == 0:
            return Node(isleaf = True)
        return checkGrid(maxLeft,maxRight,maxTop,maxBottom)


        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        
