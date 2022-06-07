import random
user_wins =0
computer_wins=0

option = ["rock" , "paper" , "sessor"]

while True:
    user_input = input("type rock/paper/sessor or Q to quit ")
    if user_input == "Q":
        break

    if user_input not in option:
        continue

    random_number =random.randint(0,2)
    computer_pick =option[random_number]
    print("computer_pick" , computer_pick + ".")


    if user_input =="rock" and computer_pick == "sessor":
        print("user won")
        user_wins =+1
    elif user_input =="paper" and computer_pick =="rock" :
        print("user won")
        user_wins =+1
    elif user_input == "sessor" and computer_pick =="paper" :
        print("user won")
        user_wins =+1

    else:
        print("you lost")
        computer_wins +=1

    print("you won" , user_wins , "." )
    print("computer won" ,computer_wins , ".")
    print("Goodbye")


