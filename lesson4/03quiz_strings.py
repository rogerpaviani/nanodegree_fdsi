# given any string 's', which of the following always have the same value as 's' ?
# (be careful, 's' could be '')

s = ''

print s

print ('a' + s)[1:]
print s + ''
print s[0] + s[1:]
print s[0:]
