#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends


#User function Template for python3

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        
            
            gcd=math.gcd(a,b)
            lcm=(a*b)//(gcd)
            lst=[lcm,gcd]
            return lst
      
      
    
                    
                
            

    
        
        # code here


#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends
