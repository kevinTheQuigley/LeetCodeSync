class Solution(object):
    def removeDuplicates(self, nums):
        k=len(nums)
        i=0
        j=0
        while i < (k-2):
            if(k>2):
                if (nums[i]==nums[i+2]):
                    nums[i:]=nums[i+1:]
                    nums.append(None)
                    k = k-1
                    i=i-1
            i=i+1
        return k

        """
        :type nums: List[int]
        :rtype: int
        """



def removeDuplicates(nums):
    k=len(nums)
    i = 0
    while i < (k-2):
        print(i,k)
        if(k>2):
            if (nums[i]==nums[i+1])&(nums[i+1]==nums[i+2]):
                nums[i:]=nums[i+1:]
                nums.append(None)
                k = k-1
                i=i-1
        i=i+1
    print(nums)
    return k
