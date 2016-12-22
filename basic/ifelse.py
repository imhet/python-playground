age = int(raw_input('Enter your age '))

if age < 6:
    print 'Hello little one'
elif age >= 6 and age < 10:
    print 'Are you enjoying school?'
elif age >= 10 and age < 13:
    print 'You are a Tween now'
elif age >= 13 and age < 20:
    print 'Now you are officially a teenager'
else:
    print 'Welcome to the real world'

# PYTHON DOES NOT HAVE A SWITCH STATEMENT

number = age
fact = 1
st = 'abc'
while age < 2:
    fact *= age
    age -= -1
else:
    print 'Python while loops have a redundant else'
print 'factorial of your age is: ', fact

# The for loop in Python essentially iterates over a sequence. This is very
# similar to the for(i : collection) loop in Java
print 'printing all integers from 1 to 5'
for i in range(1, 5):
    print i

# We can also have a stepping factor in the iteration
print 'printing alternate numbers from 1 to 21'
for i in range(1, 21, 4):
    print i
