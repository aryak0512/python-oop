import sys

if 1 != 1:
    x = int(input("enter first number :"))
    y = int(input("enter second number :"))
    print("sum is :", x + y)

'''
reading runtime args, stored in list with first element as file path
'''
args = sys.argv
print(type(args))
print(args)
# input passed 3+4 5
print(eval(args[1]))
'''
<class 'list'>
['.\\user-input.py', '3+4', '5']
7
'''
