userNumber = int(input("What size muliplication table: "))
x = range(1,userNumber + 1 )
list1 = []
list2= []
allNumbers = []
for n in x:
  list1.append(n)
  list2.append(n)
  
for i in list1:
    for j in list2:
        number = i*j
       # print(number)
        allNumbers.append(number)
allNumbers.sort()
print(allNumbers)

x = 1
biggestNumber=0
rememberedNumbers = []
rememberedNumber = ""

for i in range(len(allNumbers)):
    if i == (len(allNumbers)-1):
        break
   # print(str(allNumbers[i])+ " = is the current number")
    #print(str(allNumbers[i+1])+ " is the next number")
    
    if allNumbers[i]==allNumbers[i+1]:
      #  print(str(allNumbers[i]) + "  == "+str(allNumbers[i+1]))
        x=x+1
        if biggestNumber < x:
            biggestNumber = x
            rememberedNumber = allNumbers[i]
             
        

    else:
       # print(str(allNumbers[i]) + " does not = "+str(allNumbers[i+1]))
        print (str(allNumbers[i]) + " appears " + str(x) + " times")
        x = 1
    
    
print (str(allNumbers[len(allNumbers)-1]) + " appears 1 times")   
print(biggestNumber) 
print(rememberedNumber)
