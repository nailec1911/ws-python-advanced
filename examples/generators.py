def my_generator():
    yield 1
    yield 2
    yield 3

# Usage
gen = my_generator()
print(next(gen))  # Outputs: 1
print(next(gen))  # Outputs: 2
print(next(gen))  # Outputs: 3
# print(next(gen))  # Raises StopIteration as there are no more values




def large_range(n):
    for i in range(n):
        yield i

# the list won't be stored so it's memory efficient
gen = large_range(1000000000000000)
print(next(gen))

# can loop on infinite list
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1
