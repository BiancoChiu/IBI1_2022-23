# the calculator function
#   input value of the house and annual salary
#   judge if value is smaller than five times salary
#   return yes/no
def calculator(value, salary):
    if value <= salary * 5:
        return 'No'
    else:
        return 'Yes'


# following is the testing code
# we assume value = 180000, salary = 35000
print(calculator(180000, 35000))
# output: No
