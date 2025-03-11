class Solution:
    def sumOfDivisors(self, n):
        total_sum = 0
        for j in range(1, n + 1):
            total_sum += j * (n // j)
        return total_sum
       
    	
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends
