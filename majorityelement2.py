class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n=len(arr)
        ele1,ele2=-1,-1
        c1,c2=0,0
        for i in arr:
            if i==ele1:
                c1+=1
            elif i==ele2:
                c2+=1
            elif c1==0:
                ele1=i
                c1+=1
            elif c2==0:
                ele2=i
                c2+=1
            else:
                c1-=1
                c2-=1
        
        count1=0
        count2=0
        
        for j in arr:
            if ele1==j:
                count1+=1
            elif ele2==j:
                count2+=1
        res=[]
        if count1>n/3:
            res.append(ele1)
        if count2>n/3 and ele1!=ele2:
            res.append(ele2)
        res.sort()
        return res
            
        #Your Code goes here.


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
