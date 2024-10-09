# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        if  root ==None:
            return None
        elif root.left ==None and root.right ==None:
            return root.val
        else:
            return self._sumNumbers(root,"")
    
    def _sumNumbers(self,node,input_str):
        if node.left != None:
            le_input_str =input_str+ str(node.val)
            vl =  self._sumNumbers(node.left,le_input_str)
        else:
            vl = 0 
        if node.right!=None:
            ri_input_str =input_str+ str(node.val)
            vr = self._sumNumbers(node.right,ri_input_str)
        else:
            vr =0
        
        if node.left ==None and node.right ==None:
            input_str += str(node.val)
            print(input_str)
            return int(input_str)
        else:
            return vr+vl

        """
        :type root: TreeNode
        :rtype: int
        """
        
