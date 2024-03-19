phone_book = {}

while True:
    print("Phone Book:")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Delete contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print("\nContact added successfully.\n")
    elif choice == '2':
        name = input("Enter contact name: ")
        print(f"\nJohn's phone number is {number}\n")
        
    elif choice == '3':
        name = input("Enter contact name: ")
        if name in phone_book:
            del phone_book[name]
            print("\nContact deleted successfully.\n")
        else:
            print("\nContact not found.")
    elif choice == '4':
        break
    else:
        print("\nInvalid choice. Please try again.")
