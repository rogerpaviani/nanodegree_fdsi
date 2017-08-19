# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def set_range(a, b, c):
    big = biggest(a, b, c)
    if (big == a):
        big2 = bigger(b, c)
        if (big2 == b):
            return big - c
        else:
            return big - b
    else:
        if (big == b):
            big2 = bigger(a, c)
            if (big2 == a):
                return big - c
            else:
                return big - a
        else:
            big2 = bigger(a, b)
            if (big2 == a):
                return big - b
            else:
                return big - a
    
print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6