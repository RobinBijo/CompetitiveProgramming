#Actual Code 
'''
An Armstrong number is a number (with 'k' digits) such that the 
sum of its digits raised to 'kth' power is equal to the number itself. 
For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371. 
'''
import math
def checkArmstrong(n):
    N = len(str(n))
    dum = n
    s = 0
    for i in range(N):
        dig = dum%10
        s+= (dig**N)
        dum = dum//10
    if s == n:return True
    else:return False
print(checkArmstrong(int(input)))

# This is done in code360
import math
def checkArmstrong(n):
    N = len(str(n))
    dum = n
    s = 0
    for i in range(N):
        dig = dum%10
        s+= (dig**N)
        dum = dum//10
    if s == n:return True
    else:return False
