'''
Brute force solution:-
for i in range nums:
    for j in range nums[i:]:

Use a dictionary for faster sorting:-
num1 + num2 = target
num1 =target-num2

create a dictionary based on 
target -num2

iterate through the numbers and check if they're in the dictionary

pop each value from the dictionary as they're used.
Using a set will save storage space.





'''


class Solution(object):
    def twoSum(self, nums, target):
        dictSet = {}
        i = 0
        while len(nums)>0:
            num = nums.pop(0)
            targetNum = target-num

            di = {nums[j] : j for j in range(len(nums))}
            if targetNum in di:
                return (i,di[targetNum]+i+1)

            i = i+1
            

            

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
''''''
