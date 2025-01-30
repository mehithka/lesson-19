def squaredValues(beg,end):
    list=[]

    for i in range(beg,end):
        list.append(i**2)
    
    list_even = []
    list_odd = []

    for i in list:
        if i%2==0:
            list_even.append(i)
        else:
            list_odd.append(i)
    
    print('here is the list of even squares within specified range', list_even)
    print('here is the list of odd squares within specified range',list_odd)

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
squaredValues(num1,num2)