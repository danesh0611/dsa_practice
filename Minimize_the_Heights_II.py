#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        n=len(arr)
        arr.sort()
        min_h=arr[0]+k
        max_h=arr[-1]-k
        res=arr[-1]-arr[0]
        for i in range(n-1):
            small=min(arr[i+1]-k,min_h)
            big=max(arr[i]+k,max_h)
            if small<0:
                continue
            res=min(res,big-small)
        return res
            
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
