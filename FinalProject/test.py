class Character:
    def __init__(self, charName, race, sex, goodOrBad, support, charClass, weapons, otherOne, otherTwo, otherThree):
        self.charName = charName
        self.race = race
        self.sex = sex
        self.charClass = charClass
        self.support = support
        self.goodOrBad = goodOrBad
        self.weapons = weapons
        self.otherOne = otherOne
        self.otherTwo = otherTwo
        self.otherThree = otherThree

    def __str__(self):
        return self.charName

akshan = ["Akshan", "Human", "Male", "Good", "Fighter", "Marksman", ["Gun", "Boomerang", "Grappling Hook"], "Shirtless", "Charismatic", "Stealthy"]
amumu = ["Amumu", "Spirit", "Male", "Good", "Support", "Tank", ["Fists", "Face", "Tears"], "Gloomy", "Small", "Mummy"]

questions = {
	"Do you prefer to play as a human?": ("Yes", "No"),
	"Are you for good or for evil?": ("For good!", "For evil!!"),
        "Do you like playing as a male or female?": ("Male", "Female"),
	"Do you prefer to battle or help other people in battle?": ("Let me at 'em!", "I wanna help!")
	}

choices = []

for question in questions:
    print(question)
    print("1. " + questions[question][0])
    print("2. " + questions[question][1])
    choice = (input("Choose your answer by selecting the number above: "))
    choices.append(int(choice))

player = ["Player",0,0,0,0,0,0,0,0,0]

#sample logic on how answers will be parsed. This will change once we can implement Django and a GUI.
if choices[0] == 1:
    player[1] = "Human"
else:
    player[1] = "Non-Human"

if choices[1] == 1:
    player[2] = "Male"
else:
    player[2] = "Female"

if choices[2] == 1:
    player[3] = "Good"
else:
    player[3] = "Bad"

if choices[3] == 1:
    player[4] = "Fighter"
else:
    player[4] = "Support"

print(list(zip(player, amumu)))
print(list(zip(player, akshan)))

# zip() combines lists into a list of tuples, "i==j for i, j in" compares the tuple values, sum() then gives a total of values that match. This logic will look different once we can use relational algebra in SQL (once we understand how to implement that with Django) but the idea will be similar.
if sum(i==j for i, j in zip(player, amumu)) > sum(i==j for i, j in zip(player, akshan)):
    print("You should play as Amumu!")
elif sum(i==j for i, j in zip(player, amumu)) < sum(i==j for i, j in zip(player, akshan)):
    print("You should play as Akshan!")
else:
    print("Looks like we couldn't decide. We'll need to ask more questions. Try again!")
