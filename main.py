# takes a user input and encodes it so every number is 3 numbers higher
def encode():
    # Lucas Benedict
    new_password = ""
    password = input("Please enter a password to encode: ")
    for i in password:
        new = int(i) + 3
        new_password += str(new)
    print("Your password has been encoded and stored")
    return new_password

# takes in a password then returns the encoded and decoded versions of the password
def decode(new_password: str):
    # Chris Bowers
    original_password = ""
    for char in new_password:
        #ittrates through each character in new_password and subtracts 3 then adds it to empty string original_password
        new_password_character = int(char) - 3
        original_password += str(new_password_character)
    return print(f"The encoded password is {new_password}, and the original password is {original_password}.")

def main():
    user_input = 0
    # loops printing the menu until the user selects to quit
    while user_input != '3':
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        user_input = input('Please enter an option: ')

        # if user inputs 1 they want to encode a passsword so that function is called
        if user_input == '1':
            new_password = encode()
        # if user inputs 2 they want to decode so that function is called
        elif user_input == '2':
            decode(new_password)



if __name__ == "__main__":
    main()