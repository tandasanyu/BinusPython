def test_if():
    size = 10  # di coba 10
    if size < 10.5:  # bernilai true secara default
        print('Hasil : ', size)


# is operator
def test_identity():
    a = [1, 2, 3]
    b = [1, 2, 3]

    if a == b:
        print("This lists have the same value.")

    if a is b:
        print("This lists are the same list.")


def test_identity2():
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    print(x is z)

    # returns True because z is the same object as x

    print(x is y)

    # returns False because x is not the same object as y, even if they have the same content

    print(x is not y)

    # returns True because x is the same object as y


def else_condition():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")


def another_else():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")


def if_oneline():
    a = 200
    b = 33
    text = "a is lower than b " if a < b else "a is bigger than b"
    print(text)


def nested_if():
    x = 41

    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")


def print_list():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)


def print_string():
    for x in "banana":
        print(x, "\t")


def for_break_():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break


def continue_statement():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)


def range_function(g):
    # print(g)
    if g == 1:
        for x in range(6):
            print(x)
    elif g == 2:
        for z in range(2, 6):
            print(z)
    else:
        for y in range(2, 30, 3):
            print(y)


def else_inforloop():
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")


def nested_loop():
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)


# tugas

def whileLoop():
    total = 0
    i = 1

    while i <= 3:
        total += i
        print(i)
        i += 1
    print("Total :",total)


def primenumber():
    for num in range(10, 20):  # to iterate between 10 to 20
        for i in range(2, num):  # to iterate on the factors of the number
            if num % i == 0:  # to determine the first factor
                j = num / i  # to calculate the second factor
                print('%d equals %d * %d' % (num, i, j))
                break  # to move to the next number, the #first FOR
            else:  # else part of the loop
                print(num, 'is a prime number')


def primenumbr2():
    lower = 10
    upper = 20

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


def forwith_index():
    pets = ["cat", "dog", "budgie", "rabbit", "seahorse"]

    #    for pet in pets:
    #        print('Bagian 1 : ', pet)

    for i in range(len(pets)):
        pet = pets[i]
        if i % 2 == 0:
            print('Bagian 2 : ', pet, 'dan index : ', i, 'Merupakan Index Genap')
        else:
            print('Bagian 2 : ', pet, 'dan index : ', i, 'Merupakan Index Ganjil')


def if_nested():
    x = 41

    if x > 10:
        print("Above ten, ")
        if x > 20:
            print("and also above 20")
        else:
            print("but not 20 ")


def forrange():
    for x in range(6):
        if x == 3: break
        print(x)
    else:
        print()


def doublelit():
    adj = ["a", "b"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)


def whilestatement():
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("is no longer than 6 ")

def hellowrod(x):
    if x > 6 :
        print("Hellow World")



def sugestanswer():
    pets = ["cat", "dog", "budgie", "rabbit", "seahorse"]
    for x in pets:
        print(x)
        if x == "dog":
            break


def sugestanswer2():
    pets = ["cat", "dog", "budgie", "rabbit", "seahorse"]
    for x in pets:
        if x == "dog":
            break
        print(x)


def lenrange():
    pets = ["cat", "dog", "budgie", "rabbit", "seahorse"]
    for index in range(len(pets)):
        print ("Current : ",pets[index])