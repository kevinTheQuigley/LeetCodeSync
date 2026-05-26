
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()

        left =0
        right=0
        maxCharLen=0

        while right <len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            right+=1
            charLen=right-left
            if charLen>maxCharLen:
                maxCharLen=charLen
                print(left,right)
        
        return maxCharLen
