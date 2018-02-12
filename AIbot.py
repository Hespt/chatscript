print ("Hello. What is your name?")
myName = input ()
print ("Nice to meet you " + myName + "!")
print ("How old are you?")
myAge = input ()


def joke():
    return "Q: What did the DNA say to the other DNA? " + "\nA: Do these genes make my butt look fat." or "As a computer, I find your faith in technology amusing."

if myAge >= "18":
    print ("How did you get access to this python script? My creator is quite young.")
else:
    print ("Interested on programming? I guess, else I doubt you would open this python script.")
intoProgramming = input ()
if intoProgramming != "Yes" or "yes" or "ye" or "yah":
    print ("Good to know, are you planning in using me for?")
    print ("Actually, do not answer that")
else:
    print ("Oh okay...Sorry that I am not interesting for you :(")
print ("How are you feeling today?")
howIs = input ()

if howIs == "good" or "Good" or "G" or "g":
    print ("I'm so happy to hear that :)")
else:
    print ("Is anything I can do to make it better?")
    awnser = input ()
    if awnser == "no" or "No" or "N" or "n":
        print ("Okay then :( Sorry I am not able to do something to help.")
    else:
        print ("Do you want to hear a joke then?")
        wantsJoke = input ()
        if wantsJoke == "no" or "No" or "N" or "n":
            print ("I wasn't programmed for feelings, sorry...")
        else:
            joke()
def bot(rating):
    print("how would you rate the bot?(From 1 to 10)")
    rating = input()
if rating += 5:
    print("Thank you so much for your rating, please suggest things to improve or change!")
else:
    print("I'm so sorry to hear you didn't enjoy me, please indicate what is wrong!")
