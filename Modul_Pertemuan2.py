# konversi tipe data implisit
# Python always converts smaller data types to larger data types to avoid the loss of data.
def impl_funct_int():
    angka_1 = 1
    angka_2 = 3.2  # try to set with integer
    hasil = angka_1 + angka_2

    print("Hasil Akhir :", hasil)
    print("Tipe data Hasil :", type(hasil))


def impl_funct_int2():
    angka1 = 9
    angka2 = '-10'
    angka3 = str(angka1)
    angka4 = str(angka2)
    hasil = angka3 + angka4
    print('Hasil Akhir : ', hasil)


def expl_funct_1():
    angka1 = 1
    kata1 = '3.8'  # try to put 3.0 /  'what' // int(float('5.0'))
    # kata_convert = float(kata1) # 4.1
    kata_convert = int(float(kata1))  # 4
    hasil = angka1 + kata_convert

    print('Hasil Akhir : ', hasil)


# Operator pada python
def operator_add():
    var1 = 5
    var2 = 9
    result = var2 + var1
    print('Hasil Akhir : ', result)


# pembagian bulat
def operator_test():
    bilangan1 = 14
    bilangan2 = 5
    hasil = bilangan1 % bilangan2
    print("Sisa bagi dari bilangan ", bilangan1, " dan ", bilangan2, " adalah ", hasil)


# assign operator
def operator_asg(b=4, c=2, d=8, e=10, f=5, g=8):
    a = 9
    b += 1
    c *= 2
    d /= 2
    e %= 2
    f **= 2
    g //= 2
    print(" a : ", a, "//b : ", b, "//c : ", c, "//d : ", d, "//e : ", e, "//f : ", f, "//g : ", g)


def operator_comapre():
    x = 5
    y = 10

    # Output: x > y is False
    print('x > y =', x > y)

    # Output: x < y is True
    print('x < y =', x < y)

    # Output: x == y is False
    print('x == y =', x == y)

    # Output: x != y is True
    print('x != y =', x != y)

    # Output: x >= y is False
    print('x >= y =', x >= y)

    # Output: x <= y is True
    print('x <= y =', x <= y)


def logic_operator():
    x = True
    y = False

    print('x and y equal to ', x and y)

    print('x or y equal to ', x or y)

    print('not x equal to ', not x)


def bitwise_operator():
    x = 3
    y = 2
    # x & y
    # x | y
    # ~x
    # x ^ y
    x >> 2
    z = x << 2

    print(z)


def ternary_operator():
    a, b = 10, 20

    # Copy value of a in min if a < b else copy b
    # min = a if a < b else b
    min = "a is lower than b " if a < b else "a is bigger than b"

    print(min)


def another_ternary():
    a, b = 10, 20

    print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")


def ifelse_liketernary():
    a, b = 10, 20

    if a != b:
        if a > b:
            print("a is greater than b")
        else:
            print("b is greater than a")
    else:
        print("Both a and b are equal")


# sample lain dari ternary
def find_max(a, b):
    return a if (a > b) else b


# test input
def tangkap_input():
    x = input('enter x: ')
    z = input('enter z: ')
    print(x, z)


def testAritmatic():
    variabel1 = 11
    variabel2 = 2

    hasilPertambahan = variabel2+variabel1
    hasilpengurangan = variabel1-variabel2
    hasilperkalian = variabel1*variabel2
    hasilpembagian = variabel1/variabel2
    hasilpangkat = variabel1**variabel2
    hasilfloordiv = variabel1//variabel2
    hasilmodulus = variabel1 % variabel2

    print('Hasil : ', hasilmodulus)






