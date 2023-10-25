def main():

    def encoder():
        new_password = ""
        password = input("Please enter a password to encode: ")
        for i in password:
            new = int(i) + 3
            new_password += str(new)
        print("Your password has been encoded and stored")
        return new_password
    endcoded_password = encoder()

#decoder function needs new_password passed into it
    def decoder(new_password):
        original_password = ""
        for char in new_password:
            #ittrates through each character in new_password and subtracts 3 then adds it to empty string original_password
            new_password_character = int(char) - 3
            original_password += str(new_password_character)
            return print(f"The encoded password is {new_password}, and the original password is {original_password}.")





if __name__ == "__main__":
    main()