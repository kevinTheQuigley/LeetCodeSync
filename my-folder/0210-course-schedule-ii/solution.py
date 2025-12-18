class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def preqListGen(numCourses,prerequisites):
            preqList = [[] for _ in range(numCourses)]

            for course,prereq in prerequisites:
                preqList[prereq].append(course)
            
            return preqList
            
        preqList = preqListGen(numCourses,prerequisites)

        inVertices = [0]*numCourses

        def findInVertices(prerequisites,inVertices):
            for course,prerequisite in prerequisites:
                inVertices[course]+=1
            return inVertices
            

        inVertices = findInVertices(prerequisites,inVertices)
        
        courseStack = []
        returnStack = []
        courseCounter = 0 

        for course in range(numCourses):
            if inVertices[course]==0:
                courseStack.append(course)
        
        while len(courseStack)>0:
            courseCounter+=1
            #print(inVertices,preqList,courseStack)
            currentCourse = courseStack.pop()
            returnStack.append(currentCourse)
            for nextCourse in preqList[currentCourse]:
                inVertices[nextCourse]-=1
                #print(inVertices,preqList,courseStack)
                if inVertices[nextCourse]==0:
                    courseStack.append(nextCourse)
        if courseCounter!=numCourses:
            return []
        else:
            return returnStack


        
        


        
