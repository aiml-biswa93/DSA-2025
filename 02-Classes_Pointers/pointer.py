num1=11
num2=num1

print(num1)
print(num2)

print(id(num1)) 
print(id(num2))

num1=22

print(id(num1)) 
print(id(num2))

dict1 = {'a':1}
dict2 = dict1

print(dict1)
print(dict2)

print(id(dict1)) 
print(id(dict2))

dict1['a'] = 2

print(id(dict1)) 
print(id(dict2))



