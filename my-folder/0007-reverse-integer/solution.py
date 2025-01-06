'''
Makes sense to pop the elements off one at a time. We can check if the last value is going to exceed the allowed length before  appending it. First lets figure out the range.

'''

class Solution(object):
    def reverse(self, x):
        newNum = 0 
        y = 0 
        if x>=0:
            while x >=10:
                y+=x%10
                y*=10
                x = x//10
        else:
            while x <=-10:
                if x%10 !=0:
                    y+=10-x%10
                    y*=10
                    x = x//10  
                    if x!=0:
                        x+=1
                else:
                    y*=10
                    x = x//10 
                

        # now x is less then 10. If x is greater then zero,we can use the positive unsigned int
        if x>=0:
            if y//10>(int((2**31-1)//10 )):
                return 0
            elif y//10 == (int((2**31-1)//10 )):
                
                if x<5:
                    y=y+x
                else:
                    return 0
            else:
                y = y+x
        elif x<0:
            if -y//10<-(int((2**31)//10 )):
                return 0
            elif -y//10 == -(int((2**31)//10 )):
                print("Doing it")
                if x>-6:
                    y=-y+x
                else:
                    return 0
            else:
                y+=-x
                y=-y
        return y



        
