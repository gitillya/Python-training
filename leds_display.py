numberArray = ['#### ## ## ####',
               '  #  #  #  #  #',
               '###  #####  ###',
               '###  ####  ####',
               '# ## ####  #  #',
               '####  ###  ####',
               '####  #### ####',
               '###  #  #  #  #',
               '#### ##### ####',
               '#### ####  ####']
lines = ["", "", "", "", ""]


def print_number(number):
    j = 0
    for i in range(0, len(numberArray[number]), 3):
        lines[j] += numberArray[number][i:i + 3]
        lines[j] += " "
        j += 1


number = list(input("Please enter non-negative integer number:"))

for a in number:
    print_number(int(a))

for prn in lines:
    print(prn)
