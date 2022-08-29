a = ['apple', 'banana', 'cheery']
b = 'apple'
z = 'car'
a.append(b)
a[0]=z
print(a[0:2])
c=a
print(c)

#Here length of Print the length of the list
g=['ravi','teja','ganesh']
print(len(g))

#Print first value of the list
z=['apple','banana']
print(z[0])

#Print first 3 values of the list
f=[1,2,3,4]
print(f[0:3])

#Print first character of the String
str = "abcde"
firstThree = str[0] # getting the first 3 characters
print('first char of string is:', firstThree)

#Find length of the string
tr = "geeks"
print('Length of the string is :', len(str))

#Write a Python script to check whether a given key already exists in a dictionary
i=['apple', 'banana', 'cherry']
j='apple'
if j in i :
    print("yes 'apple' is present in the list" )
else:
    print("No 'apple' is present")

#print all items by referring to their index number:
thislist = ['apple', 'banana', 'cherry']
for i in range(len(thislist)):
    print(thislist[i])