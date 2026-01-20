def read_file():
    try:
        with open("anjan.txt", "r") as file:
            print("\n--- People Data ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Create people.txt first.")


def add_person():
    name = input("Enter name: ")
    profession = input("Enter profession: ")
    age = input("Enter age: ")
    phone = input("Enter phone: ")

    with open("anjan.txt", "a") as file:
        file.write(f"{name} | {profession} | {age} | {phone}\n")

    print("Person added successfully.")


while True:
    print("\n1. Read file")
    print("2. Add new person")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        read_file()

    elif choice == "2":
        add_person()

    elif choice == "3":
        print("Bye.")
        break

    else:
        print("Invalid option.")
