class Solution(object):
    def combinationSum(self, candidates, target):
        self.returnList = []


        self.dfs(target,candidates,0,[])
        return self.returnList
    
    def dfs(self,target,nums,index,chain):
        #print(chain,nums,index)
        if chain is None:
            chain = []

        if target ==0:
            self.returnList.append(chain)
            return 
        elif target <0:
            return
        for i in range((len(nums))):
            
            self.dfs(target - nums[i],nums[i:],i,chain+[nums[i]])


        
        

            

        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
