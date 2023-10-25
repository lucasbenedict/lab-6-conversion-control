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


if __name__ == "__main__":
    main()