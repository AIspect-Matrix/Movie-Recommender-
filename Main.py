genre = input("What is your favorite genre? (Action/Comedy/Horror): ").capitalize()
age = int(input("How old are you? "))

# All the main categories must be aligned on the far left
if genre == "Action":
    if age >= 18:
        print("I recommend watching 'John Wick'.")
    else:
        print("I recommend watching 'Spider-Man'.")

elif genre == "Comedy":
    print("I recommend watching 'The Office'.")

elif genre == "Horror":
    print("I recommend watching 'The Conjuring'.")

else:
    # This only runs if the user typed something OTHER than Action, Comedy, or Horror
    print("Sorry, I don't have a recommendation for that genre yet!")
    
