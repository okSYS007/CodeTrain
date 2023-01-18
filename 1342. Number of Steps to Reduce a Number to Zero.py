import time 


class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            
        return count

num1 = 14 #6
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
num2 = 8 #4
# Step 1) 8 is even; divide by 2 and obtain 4. 
# Step 2) 4 is even; divide by 2 and obtain 2. 
# Step 3) 2 is even; divide by 2 and obtain 1. 
# Step 4) 1 is odd; subtract 1 and obtain 0.
num3 = 123 #12

MySolution = Solution()

start = time.time() 
print(MySolution.numberOfSteps(num1))
end = time.time() - start 
print(end) 

start = time.time() 
print(MySolution.numberOfSteps(num2))
end = time.time() - start 
print(end) 
start = time.time() 
print(MySolution.numberOfSteps(num3))
end = time.time() - start 
print(end) 