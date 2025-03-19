def pet_picker():
    print("🐴  🐶  🐱  🐍  Welcome to the AI Pet Picker! 🐠  🦜  🦎")
    
    # Asking questions
    budget = input("How much can you spend per month on a pet? (low/medium/high): ").strip().lower()
    space = input("Do you have a lot of space? (yes/no): ").strip().lower()
    hobby = input("Do you want to keep your pet as a hobby? (yes/no): ").strip().lower()
    energy = input("Do you want a pet that has lots of energy (yes/no): ").strip().lower()
    time = input("Do you want a pet that needs daily attention? (yes/no): ").strip().lower()
    allergies = input("Do you have allergies? (yes/no): ").strip().lower()
    

    # Basic decision logic
    if allergies == "yes":
        pet = "Fish 🐠 or Reptile 🦎 (low risk of allergies)"
    elif budget == "low" and time == "no":
        pet = "Hamster 🐹 or Guinea Pig 🐭 (Low cost, easy to care for)"
    elif budget == "high" and space == "yes" and hobby == "no":
        pet = "Dog 🐶 (Needs space, time, and love!)"
    elif space == "no" and time == "yes":
        pet = "Cat 🐱 (Independent but loves attention)"
    elif budget == "high" and space == "yes" and energy == "yes" and hobby == "yes":
        pet = "Horse 🐴 (Energetic and loves to run all day)"
    else:
        pet = "Parrot 🦜 (Intelligent and fun, but requires effort!)"

    # Output result
    print(f"\n✨ Your perfect pet match is: {pet} ✨")
    print("Thanks for using the AI Pet Picker! 🐾")

# Run the function
pet_picker()

print("Pet care tips! 🧡")

care = input("Would you like some tips on how to take care of your pet? (yes/no): ").strip().lower()



if care == "yes":
    print("Here's a basic pet care tip:")
    print("Feed them lots of fresh water every day (unless its a fish, they have plenty of water!). 🐾")
    print("Remember, every pet is different, so make sure to research your specific pet's needs!")
else:
    print("Okay, enjoy your new pet! 🐾")