#made for father Renuka Prasad by Harshith Renukaprasad, version 1.3

class woman:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def changeName(self, name):
        self.name = name

    def classify(self, perceivedWidth):
        if(perceivedWidth <= 0):
            raise Exception('The perceived width cannot be less than or equal to 0 bro')
        elif(perceivedWidth >= 1 and perceivedWidth < 5):
            return "You got a OKL or oniko butt lady aka Fiona"
        elif(perceivedWidth >= 5 and perceivedWidth < 10):
            return "You got a SBIL or small butt lady aka Jules"
        elif(perceivedWidth >= 10 and perceivedWidth < 15):
            return "You got a NBIL or normal butt lady phew!"
        elif(perceivedWidth >= 15 and perceivedWidth < 20):
            return "You got a MIBL or medium butt lady, you're still ok I think"
        else:
            return "You got a MARBLE, a massive butt lady, run away immediately aka Mona's best friend"
        

getNamePrompt = "What is your female's name: "
name = str(input(getNamePrompt))
woman = woman(name)
checkPrompt = woman.getName() + " is your female's name, would you like to change it (Y/N): "
check = str(input(checkPrompt))
yesList = ["y", "Y", "yes", "Yes", "Howdu", "howdu"]
noList = ["n", "N", "no", "No", "illa", "Illa"]

if(check in noList):
    print("Ok, lets go on")
elif(check in yesList):
    newName = str(input("Ok, whats the new name going to be: "))
    woman = woman.changeName(newName)
else:
    print("I don't even know what that was, I'm going to assume it's the correct name")

perceivedWidth = int(input("What's the perceived width of the lady's butt (in inches, range of 0 and up): "))
ans = woman.classify(perceivedWidth)
print(ans)



        