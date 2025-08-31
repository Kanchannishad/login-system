import getpass

users_db = {}

def register():
    print("\n--- Register ---")
    username = input("Enter new username: ")
    if username in users_db:
        print("Username already exists! Try logging in.")
        return
    password = getpass.getpass("Enter new password: ")
    users_db[username] = password
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if users_db.get(username) == password:
        print("Login successful!")
        secured_page(username)
    else:
        print("Invalid username or password.")

def secured_page(username):
    print(f"\n🔒 Welcome, {username}! You are on the secured page.")
    print("Only logged-in users can access this area.\n")

def main():
    while True:
        print("\n=== Login Authentication System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
