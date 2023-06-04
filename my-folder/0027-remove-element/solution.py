class Solution(object):
    def removeElement(self, nums, val):
        k = len(nums)
        j=0
        for i in range(len(nums)):
            nums[j]=nums[i]
            j=j+1
            if nums[i] == val:
                k=k-1
                j=j-1
        nums=nums[:k]
        self.nums=nums
        return k
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
def removeElement(nums, val):
    k = len(nums)
    j=0
    for i in range(len(nums)):
        nums[j]=nums[i]
        j=j+1
        if nums[i] == val:
            k=k-1
            j=j-1
    nums=nums[:k]
    print(nums)
    return k

