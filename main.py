# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cmath

def myPow(x, y):
    return cmath.exp(y * cmath.log(x))


def allRoots(x, n):
    p = myPow(x, 1.0 / n)
    for i in range(n):
        return [p * cmath.exp(2j * cmath.pi * i)]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(myPow(-1, 0.5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
