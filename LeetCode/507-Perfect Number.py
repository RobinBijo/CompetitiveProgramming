
#Optimized Code using time complexity O(sqrt(n))
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:  # 1 is not a perfect number
            return False
        
        sum = 1  # 1 is a divisor of every number
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if i * i == num:  # if i is the square root of num
                    sum += i
                else:
                    sum += i + num // i
        
        return sum == num


#Code using o(n)
class Solution(object):
    def checkPerfectNumber(self, num):
        s = 0
        for n in range(1,num):
            if num%n == 0:#factor found
                s+= n
        if s== num:return 'true'
        else: return 'false'
ret = Solution()
print(ret.checkPerfectNumber(int(input())))
# Last 2 lines were added when i was programming in IDLE
