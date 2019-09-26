shift_value = ""
text = input("Enter your message: ")
isTrue = True
cipher = ''

while isTrue:
    try:
        shift_value = int(input("Enter a shift is an integer number from the range 1..25: "))
        if shift_value < 0 or shift_value > 25:
            raise Exception ("Your number is not in the range 1..25")
        else:
            isTrue = False
    except:
        print("Oops... Something is wrong. Try again!")

for char in text:
    print(char)

    char = char.upper()
    code = ord(char) + shift_value
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
