L = [4,5,6,7,8,9,10,8]
print('Original List: ',L)

count =0

for i in L:
    count += i

avg = count/len(L)

print('Sum = ',count)
print('average = ',avg)

L.sort()

print('the last element in the list is: ', L[-1])
