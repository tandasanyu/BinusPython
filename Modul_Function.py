def custom_try_square(line):
    if line == 0 or line == 8:
        print("*********")
    else:
        print("*       *")

def custom_try_arow(line):
    if line == 1 :
        print("   ***   ")
    elif line == 2 :
        print("  *****  ")
    else :
        print("    *    ")

# for oval shape
def diamondshape():
    row = 6
    col = 5

    for i in range(0, row):
        for j in range(0, col):
            if ((j == 0 or j == col - 1) and (i != 0 and i != row - 1)):
                print('*', end='')  # end='' so that print statement should not change the line.
            elif (((i == 0 or i == row - 1) and (j > 0 and j < col - 1))):
                print('*', end='')
            else:
                print(end=' ')  # to print the space.

        print()  # to change the line after iteration of inner loop.

# for diamond shape
def ovalshape():
    row = 6
# Upper part of hollow diamond
    for i in range(1, row+1):
        for j in range(1,row-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower part of hollow diamond
    for i in range(row-1,0, -1):
        for j in range(1,row-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def for_example():
#    for x in range(0, 10, 1):
#        print(x)
    for x in range (0,9,1):
        custom_try_square(x)
    for z in range (0,9,1):
        custom_try_arow(z)


diamondshape()
ovalshape()



def tugas1():
    print("*********      ***        *          * ");
    print("*       *    *     *     ***        * * ");
    print("*       *   *       *   *****      *   * ");
    print("*       *   *       *     *       *     * ");
    print("*       *   *       *     *      *       * ");
    print("*       *   *       *     *       *     * ");
    print("*       *   *       *     *        *   * ");
    print("*       *    *     *      *         * * ");
    print("*********      ***        *          * ");

def asterik_function_analog():
    print('*')
    print('***')
    print('**')
    print('*')

def another_ast():
    print('**')
    print('*')

def my_anotherfunction(myname):
    print(f'Hello my name is ,{myname}. Nice To Meet You !')

# simple pyramid

def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

            # ending line after each row
        print("\r")

    # Driver Code


