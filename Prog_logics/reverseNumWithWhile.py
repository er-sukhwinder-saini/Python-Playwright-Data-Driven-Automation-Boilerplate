# WAP to reverse a num using while loop


num = int(input("Enter a number to reverse===>"))
reverseNum=0
if num < 10:
    print('Enter value in more than 1 digits')  
else:
    while num > 0 :
        tempVar = num % 10
        reverseNum = reverseNum * 10 + tempVar
        num=num//10
      
print("Reverse number {}".format(reverseNum))
