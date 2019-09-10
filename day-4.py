# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def missingPositiveInt(array):
    running_lowest = 1
    for x in array:
        if x == running_lowest:
            running_lowest += 1
    return running_lowest

test_1 = [3, 4, -1, 1]
test_2 = [1, 2, 0]
print(missingPositiveInt(test_1))
print(missingPositiveInt(test_2))