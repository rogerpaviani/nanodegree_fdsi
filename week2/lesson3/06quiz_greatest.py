# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    result = 0
    while list_of_numbers:
        current_num = list_of_numbers.pop()
        if (result < current_num):
            result = current_num
    return result

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
