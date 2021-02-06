def absol_value(num):
    if num >= 0:
        return num
    else:
        return -num


def append1():
    my_list = ['geeks', 'for']
    my_list.append('geeks')
    print(my_list)


def append_single():
    my_list = ['geeks', 'for', 'geeks']
    another_list = [6, 0, 4, 1]
    my_list.append(another_list)
    print(my_list)


def extend1():
    my_list = ['geeks', 'for']
    another_list = [6, 0, 4, 1]
    my_list.extend(another_list)
    print(my_list)


def extend2():
    my_list = ['geeks', 'for', 6, 0, 4, 1]
    my_list.extend('geeks')
    print(my_list)


def list_contoh():
    text1 = "MyName"
    tuplename = ('a', 'b')
    listname = ['c', 'd']
    print(list(listname))


y = 10


def local_fucntion(kondisi1):
    x = 20

    print("Local Variabel : ", x)
    print("Global Variabel :", y)


def contoh_set():
    # working of set() on list and tuple

    # initializing list
    lis1 = [3, 4, 1, 4, 5]

    # initializing tuple
    tup1 = (3, 4, 1, 4, 5)

    # Printing iterables before conversion
    print("The list before conversion is : " + str(lis1))
    print("The tuple before conversion is : " + str(tup1))

    # Iterables after conversion are
    # notice distinct and elements
    print("The list after conversion is : " + str(set(lis1)))
    print("The tuple after conversion is : " + str(set(tup1)))


# -----------------------
# tugas 2
def swp_var():  # only work with int
    # x = 'd'
    # y = 10
    #
    # x, y = y, x
    # print("x =", x)
    # print("y =", y)

    x = 5
    y = 10

    # create a temporary variable and swap the values
    temp = x
    x = y
    y = temp

    print('The value of x after swapping: {}'.format(x))
    print('The value of y after swapping: {}'.format(y))

    print("Nama Saya : ",x," !")


# tugas3
def fizbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print("Angka yang Habis di Bagi 3 dan 5")
    elif num % 5 == 0:
        print("Angka yang Habis di Bagi 5")
    elif num % 3 == 0:
        print("Angka yang Habis di bagi 3")
    else:
        print("Angka ini = [", num, "] tidak Habis di bagi 3 dan 5")


# tugas 4
def tebak_angka():
    required_number = '18'

    while True:
        number = input("Masukan Angka Tebakan :\n")
        if number == required_number:
            print("Betul !")
            break
        else:
            print("Salah Angka, coba lagi !")

# baru sampe tugas 5
# tugas 5
def speedCheck(speed):
    speed_limit = 70
    value = speed - speed_limit
    demerit_points = value / 5
    if speed <= 70:
        print('OK')
        print(f'Points: {int(demerit_points)}')
    elif demerit_points <= 12:
        print(f'Points: {int(demerit_points)}')
    else:
        print(f'Points: {int(demerit_points)}')
        print('License suspended')


# tugas 6
def tugas6():
    num = int(input("Please choose a number to divide: "))
    listrange = list(range(1, num + 1))
    divisorlist = []

    for number in listrange:
        if num % number == 0:
            divisorlist.append(number)

    print(divisorlist)


# tugas 7
def tugas7():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for elements in a:
        if elements < 5:
            b.append(elements)
    print(b)



def tugas7_2():
    # Program to display the Fibonacci sequence up to n-th term

    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

# tugas 8 Fibonacci Number
def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    print(fib)


# Note for Fibonacci Number Function :
# This solution is using what is called the “iterative” method of computing Fibonacci numbers. This means you use
# some kind of loop to keep adding numbers together to get the next number.
# An alternative way of computing Fibonacci numbers is to use recursion, or calling the same function over and over
# in a special way, to compute the Fibonacci numbers. We will talk about this in a future exercise.
def fungsi_tugas9_1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


def fungsi_tugas9_2(x):
    return list(set(x))


# Tugas 9
def Tugas9():
    print(
        "Ketik Loop Jika ingin menyelesaikan masalah ini dengan Looping, Ketik Set jika ingin menyelesaikan dengan Sets")
    Pilihan = input("Please Chose How you want to Solve this Problem ?:")
    a = [1, 2, 3, 4, 3, 2, 1]
    if Pilihan == "Loop":
        print(fungsi_tugas9_1(a))
    elif Pilihan == "Sets":
        print(fungsi_tugas9_2(a))
    else:
        print("Pilihan yang Anda masukan tidak sesuai kriteria !")




# Tugas 10
def tugas10(x):
    y = x.split(" ")  # di isi kosong / " "
    # return y
    return " ".join(reversed(y))

    s = "".join(reversed(y))


def contoh_penggunaan_reverserd():
    # for string
    seq_string = 'Python'
    print(list(reversed(seq_string)))

    # for tuple
    seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
    print(list(reversed(seq_tuple)))

    # for range
    seq_range = range(5, 9)
    print(list(reversed(seq_range)))

    # for list
    seq_list = [1, 2, 4, 3, 5]
    print(list(reversed(seq_list)))


def contoh_join():
    # Python program to demonstrate the
    # use of join function to join list
    # elements with a character.

    list1 = ['1', '2', '3', '4']

    s = "-"

    # joins elements of list1 by '-'
    # and stores in sting s
    s = s.join(list1)

    # join use to join a list of
    # strings to a separator s
    print(s)


def contoh_split():
    num = ['1', '2']
    # print(num.split(','))

    text = 'Marvin Gaye'
    # Splits at space
    print(text.split())

    word = 'Marvin, Gaye'
    # Splits at ','
    print(word.split(','))

    word = 'Marvin:Gaye'
    # Splitting at ':'
    print(word.split(':'))

    word = 'CatBatSatFatOr'
    # Splitting at 3
    print([word[i:i + 3] for i in range(0, len(word), 3)])


def contoh_penggunaan_list():
    # Python3 code to demonstrate the
    # working of set() on list and tuple

    # initializing list
    lis1 = [3, 4, 1, 4, 5]

    # initializing tuple
    tup1 = (3, 4, 1, 4, 5)

    # Printing iterables before conversion
    print("The list before conversion is : " + str(lis1))
    print("The tuple before conversion is : " + str(tup1))

    # Iterables after conversion are
    # notice distinct and elements
    print("The list after conversion is : " + str(set(lis1)))
    print("The tuple after conversion is : " + str(set(tup1)))
