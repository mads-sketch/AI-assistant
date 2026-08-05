def greet():
    print("Hello!")
    print("Welcome!")
    print("Let's build an AI assistant!")
name = input("What is your name? ")

if name == "Madeleine":
    print("HELLO, MADELEINE! 👋")
else:
    print("Hello " + name + "! I am your AI assistant.")

try:
    with open("memory.txt", "r") as file:
        favorite_subject = file.read().strip()

    if favorite_subject:
        print("I remember your favorite subject is " + favorite_subject + ".")
    else:
        favorite_subject = input("What's your favorite subject? ")

        with open("memory.txt", "w") as file:
            file.write(favorite_subject)

        print("I'll remember that your favorite subject is " + favorite_subject + ".")

except FileNotFoundError:
    favorite_subject = input("What's your favorite subject? ")

    with open("memory.txt", "w") as file:
        file.write(favorite_subject)

    print("I'll remember that your favorite subject is " + favorite_subject + ".")

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

    elif choice == "help":
        print("Available commands:")
        print("- hello")
        print("- joke")
        print("- school")
        print("- favorite")
        print("- help")
        print("- quit")

    elif choice == "quit":
        print("Goodbye!")
        break

    else:
        print("I'm not sure how to do that yet.")

greet()
        