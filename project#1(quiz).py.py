print("This quiz is about me!")

playing = input("\nDo you want to play? \n yes or no \n   ")

if playing.lower() != "yes":
    quit()
print("\nOkay!Let's go:)")
score = 0



answer = input("\nWW2 started when Germany invaded which country?\na.Great Britain\nb.France\nc.Poland\n ").lower()
if answer == "c":
    score += 1
    print('Correct!\nNow next question')
else:
    print("Incorrect\nTry not to make mistakes")



answer = input("\nJapan launched an attack on the US mainland by using which method?\na.helium balloons\nb.biobombs\nc.atom bomb\n ").lower()
if answer == "a":
    print('Good job, right!\nDo not stop,next question')
    score += 1
else:
    print("No!\n No more mistakes please")



answer = input("\nBased on the year they were first produced, which name was given to one of Japans most highly effective fighter planes?\na.niners\nb.zeroes\nc.deuces\n ").lower()
if answer == "b":
    print('Wow, right!\nAlmost finished!, only two more questions left')
    score += 1
else:
    print("Nope!!!!")



answer = input("\nWhich city was the site of a 900-day siege during WW2?\na.Leningrad\nb.London\nc.Stalingrad\n ").lower()
if answer == "a":
    print('U r right!')
    score += 1
else:
    print("Almost right, but no")



answer = input("\nThe Germany military operation code named Valkyrie hoped to assassinate which leader?\na.Winston Chuchill\nb.Benito Mussoline\nc.Adolf Hitler\n ").lower()
if answer == "c":
    print('Right!\nFinished!!!')
    score += 1
else:
    print("NOOOO,\nFinished")



print("\nYou got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")