# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

cons_obj = cons(3, 4)
print(cons_obj.__code__.co_varnames)
print(cons_obj.__code__.co_freevars)
print(cons_obj.__closure__[0].cell_contents, cons_obj.__closure__[1].cell_contents)

# Now my brain hurts

def car(cons_obj):
    return cons_obj.__closure__[0].cell_contents

def cdr(cons_obj):
    return cons_obj.__closure__[1].cell_contents

print(car(cons(3, 4)), cdr(cons(3, 4)))