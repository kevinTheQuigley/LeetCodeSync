class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res=[]
        j = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and (j<len(nums2)):
                nums1[i]=nums2[j]
                j+=1
        nums1.sort()
        


        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
#nums1=[1,2,3,4,0]
#nums2=[1]
#print(nums1)
