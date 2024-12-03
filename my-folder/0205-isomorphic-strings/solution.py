'''
One way, create a dictionary mapping, if it's not an entry add it, if then entries not the same, return false.

one way mapping, having a dictionary that goes from one to the other
{a:b,c:d,b:b}
issue is that some keys can map to the same values
Need to create a one to one map
{a:b} -> {c:d} -> {b:a}
{b:a} -> {c:d} -> ERROR

not in either (added), not in either (added), in both, but maps to incorrect value! need to add a check
{a:b} -> {c:d} -> {b:a}
{b:a} -> {c:d} -> ERROR

Having two dictionaries, 
if key is not in either, add it to both. 
If it's just in one, return an error.

Is there a fail case for this?
I



'''

class Solution(object):
    def isIsomorphic(self, s, t):
        isoDict = {}
        revDict = {}
        for tChar,sChar in zip(s,t):
            if not (tChar in isoDict) and not(sChar in revDict):
                isoDict[tChar] = sChar
                revDict[sChar] = tChar

            elif ((tChar in isoDict) and not(sChar in revDict)) or (not (tChar in isoDict) and (sChar in revDict)):
                return False
            else:
                if isoDict[tChar] != sChar or revDict[sChar] != tChar:
                    return False

            
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
