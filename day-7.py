# Given the mapping a = 1, b = 2, ... z = 26, 
# and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3,
# since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable.
# For example, '001' is not allowed.

def decode_count(message, count=0):
    if int(message, 10) > 0 and int(message, 10) <= 26:
        count += 1

    print(count)
    if len(message) == 1:
        return count 
    else:
        midpoint = len(message) // 2
        print('step')
        return decode_count(message[:midpoint], count) + decode_count(message[midpoint:], count)

# alpha_decoder = {}
# for i in range(1, 27):
#     alpha_decoder[i] = 'cat'

print("count:", decode_count("111")) #3
print("count:", decode_count("1111")) #5
print("count:", decode_count("128")) #2
print("count:", decode_count("281")) #1