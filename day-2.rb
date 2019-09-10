# Given an array of integers, return a new array such that each element at index i of the
# new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def product(array)
    prod_array = []
    array.each_index do |i|
        non_i_array = array.slice(0, i) + array.slice(i + 1, array.length)
        prod_array << non_i_array.inject{|prod, j| prod * j }
    end
    prod_array
end

test_1 = [3, 2, 1]
test_2 = [1, 2, 3, 4, 5]
p product(test_1)
p product(test_2)