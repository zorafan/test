import re


def check(creditcard):
    checker1 = None
    checker2 = None
    charlist = list(creditcard)
    creditcardnum = ''

    if len(charlist) == 19:
        if charlist[4] == '-' and charlist[9] == '-' and charlist[14] == '-':  # d
            del charlist[4]
            del charlist[8]
            del charlist[12]
            creditcardnum = ''.join(charlist)
            if creditcardnum.isdigit():  #c
                checker1 = True
            else:
                checker1 = False
        else:
            checker1 = False
    elif len(charlist) == 16:
        creditcardnum = creditcard
        if creditcard.isdigit():  # b,c,e
            checker1 = True
        else:
            checker1 = False
    else:
        checker1 = False

    if charlist[0] == '4' or charlist[0] == '5' or charlist[0] == '6':  # a
        result = re.search(r'(\d)\1{3}', creditcardnum)
        if bool(result):
            checker2 = False
        else:
            checker2 = True
    else:
        checker2 = False

    print(bool(checker1 & checker2))


string = input("Enter a string: ")
check(string)


