numberList = [1,5,8,3,4 , 8]
#first method
 
numberList.sort()
print(numberList)


for i in range(1, len(numberList)-1):

    if  numberList[-i] == numberList[(-i-1)]:
        x = 0
    else:
        print("second largest number is:" + str(numberList[-i-1]))
        break
    

numberList = [1,6,8,8,3,4]
print(numberList)

#second method

biggestNumber = 0
secondNumber = 0

for i in numberList:
    #print(i)
    
    if  i > biggestNumber:
        secondNumber = biggestNumber
        biggestNumber=i
        
    elif i < biggestNumber and i > secondNumber:
        secondNumber = i

print("second largest number is:" + str(secondNumber))    
