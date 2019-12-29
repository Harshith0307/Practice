class renuka:
    def __init__(self, height):
        if height >= 5.9:
            print("You are lying, bye bye")
        else:
            print("Ok good start, no falsifications")    
    def birthday(self, date):
        if date == "12/28/1975":
            print("Happy Birthday, great appa.")
        else:
            print("Come on, thats not your birthday. :(")
    def insist(self, num):
        for i in range(0,num):
            print("This is an insisting message for guitar center on monday, 12/30/19")


password = str(input("Enter the password : "))
if password == "Harsha_is_the_great":
    a_var = renuka(float(input("Height as a float : ")))
    a_var.birthday(str(input("Birthday in MM/DD/YYYY : ")))
    a_var.insist(int(input("Favorite Number... GO : ")))
else:
    exit()

