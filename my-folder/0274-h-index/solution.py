class Solution(object):

    def hIndex(self, citations):
        n = len(citations)
        hashList=[0]*(n+1)

        for i in citations:
            if i >n:
                hashList[n]+=1
            else:
                hashList[i]+=1
        print(hashList)
        counter = 0 
        for i in range(n+1):
            j = n-i
            print(j,counter)
            counter += hashList[j]
            if j<=counter:
                return(j)



        """
        :type citations: List[int]
        :rtype: int
        """
        
