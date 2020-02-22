if __name__ == '__main__':
    s = input()
    print any([char.isalnum() for char in S]) #This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    print any([char.isalpha() for char in S]) #This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    print any([char.isdigit() for char in S]) #This method checks if all the characters of a string are digits (0-9).
    print any([char.islower() for char in S]) #This method checks if all the characters of a string are lowercase characters (a-z).
    print any([char.isupper() for char in S]) #This method checks if all the characters of a string are uppercase characters (A-Z).