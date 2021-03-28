#SyntaxError: unexpected EOF while parsing

#for i in range(100):

for i in range(100):
    pass

#SyntaxError: invalid syntax

#print
#for i in range(10)
    #print(i)
#a = 0
#if a = 0:
    #print(a)

print()
for i in range(10):
    print(i)
a = 0
if a == 0:
    print(a)

#TypeError: must be str, not int

#a = 5
#print("a equals " + a)

a = 5
print("a equals " + str(a))


#NameError: name 'a1' is not defined

#print(a1)

a1 = 1
print(a1)

#UnboundLocalError: local variable 'a' referenced before assignment

# def do_something():
#     print(pi)
#     pi = 3.14

# do_something()

def do_something():
    pi = 3.14
    print(pi)

do_something()

#IndentationError: expected an indented block

# if True:
# print(True)

if True:
    print(True)

    