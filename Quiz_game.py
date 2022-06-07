print("welcome to my computer quiz")
playing =input("Do you want to play? ")
if playing != "yes":
    quit()
else:
    print("ok let's start the game")
score = 0

answer = input("who is the father of computer? ")
if answer == "Charles Babbage":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")



answer = input("what is mean of GPI? ")
if answer == "Graphical user interface":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")


answer = input("In which type of computer, data are represented as discrete signals? ")
if answer == "Digital Computer":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
    

answer = input("Scientific Name of Computer? ")
if answer == "Sillico sapiens":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")


answer = input("Who developed the first electronic computer? ")
if answer == "J.V. Atansoff":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
print ("you got  " +  str(score) + "question correct")
print ("you got  " +  str(score/5 *100) + "%")