import random
import string
import sys 
# variables
def string_generator(size=8, string=string.ascii_letters + string.digits):    
    return ''.join(random.choice(string) for _ in range(size))
    
#Allows the user to input how many EC2 instances they want
number = int(input("Enter the amount of EC2 instances: "))    
    
#Allows the user to choose the department name they want for their EC2 instances
department = input("Choose from one of these departments: Marketing, Accounting, FinOps: ")  


for _ in department:

    if department == "Marketing" or department.lower() == "marketing" :
        break

    elif department == "Accounting" or department.lower() == "accounting" :

        break

    elif department == "FinOps" or department.lower() == "finops" :
        break

    else:
        print("This generator is restricted to specific departments.")
        raise SystemExit
        sys.exit()


if number < 1:
    print("Please enter number greater than 0 ")
elif number > 0:
    print("")
    


for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = unique_name + "-" + string_generator()
    print("Your EC2 Instance's names will be: ", EC2_unique_name)
    
print ("\nYou have successfully created " + str(number) + " EC2 random name generators.")