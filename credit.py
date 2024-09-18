from cs50 import get_int
from sys import exit


def main():
    creditNum = str(get_number())
    numLength = len(creditNum)
    # print(creditNum[len(creditNum) -1])

    if numLength not in [13, 15, 16]:
        print("INVALID\n")
        exit(1)

    if luhns_algorithm(creditNum) % 10 != 0:
        print("INVALID\n")
        exit(2)

    get_cardType(creditNum)


def get_number():
    # scope does not matter in python thus we do not need to
    # declare n outside the while loop
    while True:
        try:
            n = get_int("Number: ")
            if n > 0:
                break
        except ValueError:
            print("Please type an integer!")
    return n


def luhns_algorithm(number):
    # create a list of every other digit starting with the second to last digit
    list1 = number[len(number) - 2 :: -2]
    # print(list1)

    # makes all strings in list1 into ints
    list1 = map(int, list1)
    # multiply each element by 2
    list1 = [i * 2 for i in list1]
    # convert list1 back to list of strings
    list1 = map(str, list1)
    # make list1 a single string
    list1 = "".join(list1)

    # create a list of every other digit starting with the last digit
    list2 = number[len(number) - 1 :: -2]
    # print(list2)
    n = 0
    for i in range(len(list1)):
        n += int(list1[i])

    for i in range(len(list2)):
        n += int(list2[i])
    # print(n)
    return n


def get_cardType(number):
    # print(number[0:2])
    if number[0:2] in ["51", "52", "53", "54", "55"]:
        print("MASTERCARD\n")
        exit(3)

    if number[0:2] in ["34", "37"]:
        print("AMEX\n")
        exit(3)

    if number[0] in ["4"]:
        print("VISA\n")
        exit(3)

    print("INVALID\n")


main()
