# WAP to enter product of natural num
prodNum=1
num = int(input('Enter natural number'))
if num<=0:
    print('Enter valid natural number')
else:
    while(num>0):
        prodNum = prodNum * num
        num = num-1 
print('Product of natural num is {}'.format(prodNum))

    