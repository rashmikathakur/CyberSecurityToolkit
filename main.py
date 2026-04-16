import os

def main_menu():
    while True:
        print("\n==============================")
        print("   CYBER SECURITY TOOLKIT")
        print("==============================")

        print("1. Port Scanner")
        print("2. Network Scanner")
        print("3. Banner Grabber")
        print("4. Vulnerability Checker")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            os.system("python3 port_scanner.py")

        elif choice == "2":
            os.system("python3 network_scanner.py")

        elif choice == "3":
            os.system("python3 banner_grabber.py")

        elif choice == "4":
            os.system("python3 vulnerability_checker.py")

        elif choice == "5":
            print("\nExiting Toolkit...")
            break

        else:
            print("\nInvalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
