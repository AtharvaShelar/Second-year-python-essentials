#program to perform basic operations
a = int(input("Enter a number"))
b = int(input("Enter another number"))
#addition
sum = a + b
sub = a - b
mul = a * b
div = a/b
fdiv = a//b
exp = a**b
mod = a%b
print("The sum of ",a," and ",b," is",sum)
print("The subtraction of ",a," and ",b," is ",sub)
print("The multiplication of ",a," and ",b," is ",mul)
print("The division of ",a," and ",b," is ",div)
print("The floor division of ",a," and ",b," is ",fdiv)
print("The modulus of ",a," and ",b," is ",mod)
print(a," to the power of ",b," is ",exp)