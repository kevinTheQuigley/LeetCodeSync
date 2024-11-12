'''
[2,7,9,3,1,5]
[1,2,3,4,5,6]
start at house 1, check how much gets robbed
2, you can choose 0 or 0
at house 2, check how much can be robbed
7, you can choose 0 or 0
at house 3, you have to skip adding 7,but you can take 2
2+9 = 11, you can choose 0 or 2
at house 4, you can choose either 2 or 7. (robbed and skipped)
7+3 = 10
at house 5, you can choos either 11 or 7
12
at house 6, you can choose either 10 or 11
12


nextRobbed, nextSkipped, robbed, skipped
0           0            0       0
0           0            0       0
0           0            0       0
0           0            0       0
0           0            0       0
0           0            0       0
'''

class Solution(object):
    def rob(self, nums):
        robbed,skipped = 0,0
        #Imagining it like DP list
        for num in nums:
            
            newRobbed = num+robbed
            newSkipped = max(robbed,skipped)


            print(robbed,skipped,newRobbed,newSkipped)

            robbed,skipped = newSkipped,newRobbed
        

            
        return max(robbed,skipped)




        """
        :type nums: List[int]
        :rtype: int
        """
        
