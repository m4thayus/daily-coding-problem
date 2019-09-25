# Given a list of integers, write a function that
# returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative. <===== Key

# For example, [2, 4, 6, 2, 5] should return 13, 
# since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, 
# since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def non_adj_sum(array):
    even_sum = 0
    odd_sum = 0
    for i in range(len(array)):
        if i % 2 == 0:
            even_sum += array[i]
        else:
            odd_sum += array[i]
        print("Odd:", odd_sum)
        print("Even:", even_sum)

    if odd_sum > even_sum:
        return odd_sum
    else:
        return even_sum

test_odd = [2, 4, 6, 2, 5]
test_even = [5, 1, 1, 5]

print(non_adj_sum(test_odd))
print(non_adj_sum(test_even))