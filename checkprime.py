from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the ques
from math import *

# Read input as specified
n = int(input())
p=0



if n <= 1:
    print("NO")
for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        p=1
        break
        
            
   

# For each number from 1 to n, check if it's prime

if p==0 and n!=1:
    print("YES")
if p>0 :
    print("NO")

