def playgame():#q
    user_input = input("Enter 'p' to play and 'q' to quit: ")
    while True:

        if user_input == "p":
            print("hello")
            user_input = input("Enter 'p' to play and 'q' to quit: ")
        elif  user_input == "q":
            print("You pressed 'q' so quitting the game")
            break
        else:
            print(f"You pressed '{user_input}' which is an invalid option in the game")
            user_input = input("Enter 'p' to play and 'q' to quit: ")


playgame()
