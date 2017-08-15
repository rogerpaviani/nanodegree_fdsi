# 23 quiz variables string find
# which of the following always has the value '0' ?

s = '<any string>'

print s.find(s)
print s.find('s') #!!!!!!!!!!!!!! retorna valor 5, neste exemplo
print 's'.find('s')
print s.find('')
print s.find(s + "!!!") + 1