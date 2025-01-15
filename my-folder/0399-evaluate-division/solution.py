from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(dict)
        for (x,y),value in zip(equations,values):
            d[x][y]= value
            d[y][x]=1/value

        returnList = []
        def dfs(key,target,multiplier,s):
            if key not in s:
                s.add(key)
                if target in d[key].keys():
                    return (d[key][target]*multiplier)
                else:
                    #print(d[key].keys(),s)
                    vals = []
                    for newKey in d[key].keys():
                        vals.append(dfs(newKey,target,multiplier*d[key][newKey],s))

                    for val in vals:
                        if val>0:
                            vals = [val]
                    return sum(vals)     
            else:
                return 0

        for query in queries:
            start = query[0]
            end = query[1]

            if not (start in d.keys() or end in d.keys()):
                returnList.append(-1)
            elif start ==end:
                if not (d[start] or d[end]):
                    returnList.append(-1)
                else:
                    returnList.append(1)
                
            else:
                s = set()
                res = dfs(start,end,1,s)
                if res ==0:
                    returnList.append(-1)
                else:
                    returnList.append(res)

        return returnList

        
