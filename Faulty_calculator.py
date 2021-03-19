#Faulty Calculator
print("Enter the first number :")
x = int(input())
print("Enter the second number :")
y = int(input())
print("select the desired operater :\n""1:addition\n""2:subtraction\n""3:multiplication\n""4:division")
z = int(input())
if (x==56 and y==9 and z==1):   #wrong calculations
    print("addition of numbers is 77")
elif (x==45 and y==3 and z==3):   #wrong calculations
    print("multiplication of numbers is 555")
elif (x==56 and y==6 and z==4):   #wrong calculations
    print("division of numbers is 4")
elif (z==1):
    print("addition of numbers is",x+y)
elif (z==2):
    print("subtraction of numbers is",x-y)
elif (z==3):
    print("multiplication of numbers is",x*y)
elif (z==4):
    print("division of numbers is",x/y)
elif z>4:
    print("invalid selection")
