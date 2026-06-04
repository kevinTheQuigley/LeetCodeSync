class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bl=0
        br=len(nums)-1

        while bl < br:
            m = (bl + br)//2

            if nums[m]==target:
                return m
            if nums[bl]>nums[m]:
                # This is the unsorted side, check the other side!
                if nums[m] < target <= nums[br]:
                    bl=m+1
                else:
                    br=m-1
            else:
                if nums[bl] <= target < nums[m]:
                    br=m-1
                else:
                    bl=m+1

        if nums[(bl + br)//2]==target:
            return (bl + br)//2
        else:
            return -1

