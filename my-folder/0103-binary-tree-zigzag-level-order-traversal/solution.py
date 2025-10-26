
from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level=1
        currentLevel = [root]
        returnList = [[root.val]]

        while len(currentLevel)>0:
            nextLevel = deque([])
            appendList = []

            if level %2:
                while len(currentLevel)>0:
                    node = currentLevel.pop()
                    if node.right:
                        appendList.append(node.right.val)
                        nextLevel.append(node.right)
                    if node.left:
                        appendList.append(node.left.val)
                        nextLevel.append(node.left)
            
            else:
                while len(currentLevel)>0:
                    node = currentLevel.pop()
                    if node.left:
                        appendList.append(node.left.val)
                        nextLevel.append(node.left)
                    if node.right:
                        appendList.append(node.right.val)
                        nextLevel.append(node.right)
            if appendList:
                returnList.append(appendList)
            currentLevel = nextLevel
            level+=1

        return returnList


