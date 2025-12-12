# print((-7)**2)
# print(round(23.23))
# print(abs(-23))
abs # it does not give me error the reason we will learn further

# concatenation
# print("Hello " + "," + "World" + "!")
# print(len("Hello World" * 4)) 
# the other arithmetic operator do not work with string

# print(round(1456456234/3,9))
# print(round(42.5))
# print(round(43.5))

# print(3++3)

print(type(type))
'''
The following questions give you a chance to practice writing arithmetic expressions:
1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
mile.
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
pace in seconds per mile?
4. What is your average pace in minutes and seconds per mile?
5. What is your average speed in miles per hour?
'''
# print((42 * 60) + 42)
# print(10/1.61)
# print( ((42 * 60) + 42) /(10/1.61))
# print( (((42 * 60) + 42) /(10/1.61)) % 60)
# print((10/1.61)/(((42 * 60) + 42)/3600))

# # Variables
# import math
# message = ("somthing completely different")
# print(message )
# print(math.pow(2,2))
# # print(math.pow('123')) gives error
# x = y = 1;

'''
Part 1. The volume of a sphere with radius r is 4/3πr3. 
What is the volume of a sphere with radius 5? Start with a variable named
radius and then assign the result to a variable named volume. Display the
result. Add comments to indicate that radius is in centimeters and volume
is in cubic centimeters.
'''
# Radius is in centimeters.
radius = 5
# Volume is in cubic centimeters.
volume = (4/3) * (22/7) * (radius**3)
result = volume
print(result)

'''
Part 2. A rule of trigonometry says that for any value of 
Let’s see if it’s true for a specific value of x like 42.
x, (cos x)**2 + (sin x)**2 = 1.
Create a variable named x with this value. Then use math.cos and math.sin to com
pute the sine and cosine of 
x
, and the sum of their squares.
The result should be close to 1. It might not be exactly 1 because floating-point arith
metic is not exact—it is only approximately correct.
'''
import math

# x = 42
# sin = math.sin(x)
# cos = math.cos(x)

# square_sum = sin**2 + cos**2
# print(sin)
# print(cos)
# print(square_sum)

'''
Part 3. In addition to pi, the other variable defined in the math module is e, which
represents the base of the natural logarithm, written in math notation as 
. If you are
not familiar with this value, ask a virtual assistant “What is math.e?” Now let’s com
pute 
e
e2
 three ways:
1. Use math.e and the exponentiation operator (**).
2. Use math.pow to raise math.e to the power 2.
3. Use math.exp, which takes as an argument a value, 
x
, and computes 
ex
.
You might notice that the last result is slightly different from the other two. See if you
can find out which is correct.
'''

e = math.e
print(e**3)
print(math.pow(e,3))
print(math.exp(3))