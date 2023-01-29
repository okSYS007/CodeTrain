from time import perf_counter

def example():
    rez = 0
    nums = [num for num in range(1000000)]

    for num in nums:
        rez += num
    print(rez)

def sumexample():
    nums = [num for num in range(1000000)]
    print(sum(nums))

start = perf_counter()
example()
print(f"time: {(perf_counter() - start):.02f}")

start = perf_counter()
sumexample()
print(f"time: {(perf_counter() - start):.02f}")
