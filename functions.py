def add_sub(x, y):
    a = x + y
    b = x - y
    return a, b


r1, r2 = add_sub(3, 2)
print(r1, " ", r2)
print("=======================")
'''
passing args to function
note: python is neither call by value, nor call by reference
'''


# here age is assigned a default value if not passed in call
def person(name, age=18):
    print("name =", name, end=" ")
    print(age)


person('aryak', age=23)
person(name='aryak')
print("=======================")
'''
variable arguments passed to add function *
the variable used for variable arguments in python is tuple
'''


def add(*nums):
    print(type(nums))
    ans = 0
    for i in nums:
        ans += i
    print("sum =", ans)


add(2, 3)
print("=======================")
'''
keyword arguments
abbreviated as : kwargs
use keywords in function call for varargs and specify ** in actual method signature
'''


def person(name, **data):
    print(data.items())
    print(type(data.items()))
    for k,v in data.items():
        print(k,v)


person(name="aryak", age=23, city="mumbai")
print("=======================")
