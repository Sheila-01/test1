# Number1 

def calculateVolume(radius, height):                            #creating a function to calculate the volume
    pi = 3.14                                                   #making pie a constant
    return pi * radius *radius *height
   
y = calculateVolume(radius = int(input("Enter radius: ")),height = int(input("Enter height: ")))  #assigning the function with the positional argumnets to y

print("Your volume is ", y)                                     #displays the volume