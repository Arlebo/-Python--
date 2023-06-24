ii = 0
array_y = [2,4,3,5,7,9,1]
while [ii<6]:
    print ('array_y ', [ii], ' : ', array_y [ii])
    ii = ii+1


for i in range (5,10):
    print (i*i)
print ('---------------')

array_a = ['one', 'two', 'three', 'some', 'any']
for i in array_a:
    print(i)
print ('---------------')

array_b = [-4, 10,-8, 1.2, 100, 5-30]
for i in array_b:
    if (i>0):
        print (i)
print('---------------')

array_c = [5,4,2,4,-2,-7, 77]
for i in array_c:
    if (i==77):
        print ('Нашли 77!')
        break
else:
    print ('Не нашли! :(')
print ('---------------')

