class Solution:
    def fib(self, n: int) -> int:
        a=0
        nxt=1
        if n==1:
            return 1
        elif n==0:
            return 0
        else:
            for i in range(2,n+1):
                x=nxt
                nxt=nxt+a
                a=x
           
        return nxt
    
        


        
