def checkArmstrong(n):
    #write your code here !!!!!!!!!
    num=str(n)
    m=n
    k=len(num)
    s=0
    digit=0
    for i in range(k):
        digit=n%10
        s=s+digit**k
        n=n//10
    if m==s:
        return True
    else:
        return False

        
