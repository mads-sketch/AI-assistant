name = input("What is your name? ")

if name == "Madeleine":
    print("Hello Madeleine! It's nice to see you again.")
else:
    print("Hello " + name + "! I am your AI assistant.")

while True:
    choice = input("What do you want to do? ")

    if choice == "hello":
        print("HELLO, MADELEINE! 👋")
    elif choice == "joke":
        print("Why did the computer go to the doctor? It had a virus! 😂")
    elif choice == "school":
        print("Time to lock in! 📚")
    elif choice == "favorite":
        print("My favorite thing is helping Madeleine build this AI!")
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("I'm not sure how to do that yet.")