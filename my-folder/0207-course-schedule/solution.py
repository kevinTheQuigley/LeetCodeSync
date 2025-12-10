class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def genReqList(prerequisites):
            reqList=[ [] for _ in range(numCourses)]
            for (course,prereq)  in prerequisites:
                reqList[prereq].append(course)
            return reqList
            
        
        state = [0]*numCourses
        reqList = genReqList(prerequisites)

        def hasCycle(course)->bool:
            if state[course]==1:
                return False
            if state[course]==-1:
                return True
            
            state[course]=-1
            for pres in reqList[course]:
                if hasCycle(pres):
                    return True
            state[course]=1
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True
