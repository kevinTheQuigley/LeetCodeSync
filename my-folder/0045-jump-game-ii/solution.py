class Solution(object):
    def jump(self, nums):
        #def def_value(): 
        #    return "Not Present"
        curPos = 0 
        le = len(nums)-1
        jumps = 0
        #print("curPos,nextPos,jumps,le,maxJump")
        while curPos<le:
            maxJump = nums[curPos]
            nextPos = maxJump +curPos
            if nextPos >=le:
                return jumps+1
            #elif nextPos >=le:
            #    return jumps+1
            for j in range(nums[curPos]+1):
                if nums[curPos+j]+j>maxJump:
                    nextPos = curPos +j
                    maxJump = nums[curPos+j]+j
                #print(curPos,nextPos,jumps,le,maxJump)
            jumps+=1
            curPos = nextPos

        return jumps
