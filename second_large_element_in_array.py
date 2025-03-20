#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        first,second=-1,-1
        for i in arr:
            if i>first:
               second,first=first,i
            elif i>second and i!=first:
                second=i
        if first==second:
            return -1
                
        return second
                
        # Code Here
