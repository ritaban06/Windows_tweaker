# Import the individual tweak modules here (e.g., change_display_resolution.py, change_display_brightness.py, etc.)
# Make sure these modules are placed in the same directory as the menu.py script.

def print_menu():
    print("\nPlease select a tweak to apply:\n")
    print("1. Change Display Resolution")
    print("2. Adjust Display Brightness")
    # Add more tweak options here as needed

def get_user_choice():
    while True:
        choice = input("Enter the number corresponding to the tweak you want to apply (0 to exit): ")
        if choice.isdigit():
            return int(choice)
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    print_menu()

    while True:
        user_choice = get_user_choice()

        if user_choice == 0:
            print("Exiting...")
            break

        # Execute the selected tweak based on user_choice
        if user_choice == 1:
            import change_display_resolution
            # Call the function to perform the change display resolution tweak

        elif user_choice == 2:
            import change_display_brightness
            # Call the function to perform the change display brightness tweak

        # Add more elif blocks for other tweak options

        else:
            print("Invalid choice. Please select a valid tweak.")
