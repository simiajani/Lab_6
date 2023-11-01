#encode funtion
def encode(password):
    new_password = ""
    for num in range(password):
        new_num = str((int(num) + 3) % 10)
        new_password += new_num
    return password

def decode(encoded_password): #subtracts 3 from each integer and decodes the encoded password
    decoded_password = ''
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        decoded_password += new_digit
    return decoded_password
def decode(password):
    decoded_password = ""
    for num in password:
        og_password = int((str(num) - 3) % 10)
        decoded_password += og_password
    return password


#decoding and encoding menu
#while loop
if __name__ == "__main__":

    menu = True
    while menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        print("Please enter an option:", end="")
        option = input()
        print("Please enter your password to encode:", end="")
        password = input()

        if option == 1:
            #encode password
            password = input()
            new_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            #decode password
            decoded_password = decode(new_password)
            print("Here is your encoded password:", new_password, "Here is your decoded password:", decoded_password)

        elif option == 3:
            #quit function
            menu = False
            exit()
