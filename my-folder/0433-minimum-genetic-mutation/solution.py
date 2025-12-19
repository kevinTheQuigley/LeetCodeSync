class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if len(bank)==0:
            return -1
        def mutationIsPossible(currentGene,nextGene):
            counter=0
            for i in range(8):
                if currentGene[i]==nextGene[i]:
                    counter+=1
            if counter >=7:
                return True
            else:
                return False
            
        geneStack= [startGene]
        def checkEndGene(currentGene):
            return (currentGene==endGene)

        counter=0
        def mutateGenes(currentGene,bank,counter):
            if checkEndGene(currentGene):
                return counter

            counter+=1
            possiblePaths=[]

            for i in range(len(bank)):
                nextGene= bank[i]
                if mutationIsPossible(currentGene,nextGene):
                    nextPath = mutateGenes(nextGene,bank[:i]+bank[i+1:],counter)
                    if nextPath:
                        possiblePaths.append(nextPath)

            if possiblePaths:
                return min(possiblePaths)
            else:
                return None
            
        
        res = mutateGenes(startGene,bank,counter)
        if res:
            return res
        else:
            return -1



                
                
                
        
