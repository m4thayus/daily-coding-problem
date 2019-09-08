#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

def add_up(array, k)
    hash = {}
    array.each do |ele|
        match =  k - ele
        if hash[match]
            return true
        end
        hash[ele] = "cat"
    end
    return false
end

test = [10, 15, 3, 7]
puts add_up(test, 17) == true
puts add_up(test, 31) == false