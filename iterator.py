# iterators:    data structure to store infinite data

# a for is syntactic sugar of this

# creating iterator
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
           13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
my_iter = iter(my_list)

# iterating an iterator
while True:
    try:
        element = next(my_iter)
        print(element)
    # if we run out of iterators, we break
    except StopIteration:
        break
