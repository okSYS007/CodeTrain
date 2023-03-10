# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #FizzBuzz
        rez = []

        for x in range(n):
            num = x+1
            if num % 3 == 0 and num % 5 == 0:
                rez.append("FizzBuzz")
            elif num % 3 == 0:
                rez.append("Fizz")
            elif num % 5 == 0:
                rez.append("Buzz")
            else:
                rez.append(str(num))

        return rez


test1 = 3 #["1","2","Fizz"]
test2 = 5 #["1","2","Fizz","4","Buzz"]
test3 = 15 #["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

MySolution = Solution()
print(MySolution.fizzBuzz(test1))
print(MySolution.fizzBuzz(test2))
print(MySolution.fizzBuzz(test3))