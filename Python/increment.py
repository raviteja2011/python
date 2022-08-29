# Print First 10 natural numbers using while loop

i = 1  # INITIALIZE
while i <= 10:  # Check condition with Comparison Operator
    print(i)
    i += 1  # Increment the value with Assignment Operator

n = 10
g = 1
print('Natural numbers up to', n)
while g<=n:
	print(g)
	g+=1
#reverse order
wordList = ['hi', 'hello', 'this', 'that', 'is', 'of']
s = len(wordList)-1
# Iterate till 1st element and keep on decrementing s
while s>= 0 :
   print(wordList[s])
   s -= 1

list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)
