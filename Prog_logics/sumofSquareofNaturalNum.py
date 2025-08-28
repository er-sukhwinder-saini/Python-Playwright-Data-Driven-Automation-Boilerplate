#WAP to sum of square of natural number

naturalNum = int(input("Enter natural number===>"))
sumOfSquare=0

if naturalNum <= 0:
    print('Enter correct natural number')
else:
    while naturalNum>0:
        sumOfSquare=sumOfSquare + (naturalNum*naturalNum)   
        naturalNum=naturalNum-1  
    print(sumOfSquare)
    
    