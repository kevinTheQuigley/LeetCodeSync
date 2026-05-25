class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        nums.sort()
        returnNums=[]
        nSet=set()

        for i in range(n):
            l=i+1
            r=n-1

            while l<n and l!=r:
                if nums[i]+nums[l]+nums[r]==0 and not (nums[i],nums[l],nums[r]) in nSet:
                    returnNums.append([nums[i],nums[l],nums[r]])
                    nSet.add((nums[i],nums[l],nums[r]) )
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return returnNums
            
