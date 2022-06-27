import random
print("Hello readername")

readername = input("What is your name?\n")

print(f"Hello {readername}")

names = ["Inshall","Kerry","Karen","Ali"]
places = ["America","Australlia","Pakistan","Italy"]
quests = ["Slay the dragon","Awesome man","Hello how are you"]
roles = ["Hello what are you doing","what is your name","is you are"]

randomname = random.choice(names)
randomplace = random.choice(places)
randomquest = random.choice(quests)
randomrole = random.choice(roles)

story = "Once upon a time was a " + randomrole + " called " + randomname + " "
print(story)