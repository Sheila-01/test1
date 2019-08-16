#number5 
def myNumbers(): 
    numbers = max(300,99,45,67,2,3,4,89)                                        #my turple of numbers with the max argument

    return numbers                                                             #returns the function body

myNumbers()                                                                   #calling the function on line 2

print("The highest number in the tuple is:",myNumbers())                       #prints the highest number

#Solution 2:
def largest(*numbers):                                                      #creating a function
    largeNum = 0
    for item in numbers:                                                    #looping through the numbers
        if item > largeNum:                                                 #if current large item is greater, replace
            largeNum = item

    return largeNum

print(largest(23,45,900,7000,54,23,21,1))                                  #The list of numbers
