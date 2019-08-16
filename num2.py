#number2 
#python program to loop through a list and print second number until list is empty

myList = [1,2,34,12,77,66,43,23,90,48] 

for position in range(len(myList)):        #loops through the list
    if len(myList)>1:                      #checks list length
        removedItem = myList.pop(1)        #removes the second item
        print(removedItem)                 #prints the removed item
