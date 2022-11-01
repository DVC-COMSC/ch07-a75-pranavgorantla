
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# printing original lists
print("Original list : " + str(num1))
print("Original sub list : " + str(num2))
 
# using all() to
# check subset of list
flag = 0
if(all(x in num1 for x in num2)):
    flag = 1
 
# printing result
if (flag):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")
