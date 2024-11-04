"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

What about using dictionaries?
for each node, we have two dictionaries
cloneNodes
cloneNeighbours

Initially, a clone of the node is created; This is added to a dictionary.
Then the two neighbours are added as newNodes to the cloneNeighbours, without adding anything to their neighbour value.

Then a recursive function could work through each neighbour.
If it's not added to the cloneNode dict, it get's added. 
for a neighbour, if the neighbour is present in cloneNode, it's added to the neighbours dict

Want to watch out for an endless loop
"""




class Solution(object):
    def cloneGraph(self, node):
        cloneDict = {}

        def cloner(node):
            if node is None:
                return None
            
            clone = Node(node.val)
            cloneDict[node] = clone

            for neighbor in node.neighbors:
                if neighbor in cloneDict:
                    clone.neighbors.append(cloneDict[neighbor])
                else:
                    clone.neighbors.append(cloner(neighbor))
            return clone
        
        return cloner(node)

                    
''''''
