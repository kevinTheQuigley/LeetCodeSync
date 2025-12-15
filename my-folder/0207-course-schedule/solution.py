
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def genPreqList(numCourses,prerequisites):
            preqList = [[] for _ in range(numCourses)]

            for (course,prereq) in prerequisites:
                preqList[prereq].append(course)

            return preqList

        preqList = genPreqList(numCourses,prerequisites)

        courseStatus = numCourses*[0]

        def hasCycle(course):
            if courseStatus[course]==-1:
                return True
            elif courseStatus[course]==1:
                return False
            
            courseStatus[course]=-1

            for nextCourse in preqList[course]:
                if hasCycle(nextCourse):
                    return True
                
            courseStatus[course]=1
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True
