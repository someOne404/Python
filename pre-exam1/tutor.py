

def a():
    global b
    b = 1
    c = 2
    return b+c

print(a()*2)

#b = 5
c = 6
print(b)
print(c)

def hey1():
    str = "Hello world"
    return str

def hey2():
    print("hey")

print(hey1())
hey2()



def person(name1, age1):
    age1 = int(age1)
    name1 = name1 + "heyyyyyyyyyy"
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    num = 3
    description = "Your name is: " + str(name) + " " + str(name1) + ", and your age is " + str(int(age) + age1 + num)
    return description

print(person("Jack", 3))


def f():
    #a = input("Please enter 1st str")
    #b = input("Please enter 2nd str")
    a = 'Hello'
    b = "Hello"
    ans = "I have a dream"
    return a==b

print(f())



a = 8.99
print(int(a))
n = 101
print(n % 2 != 0)
n2 = 78.2
print(n2 // 2)