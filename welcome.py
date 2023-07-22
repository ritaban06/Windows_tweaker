import os
import subprocess

def is_system_restore_enabled():
    try:
        result = subprocess.check_output(["wmic", "restore", "get", "disablestatus"])
        lines = result.decode("utf-8").strip().split("\n")
        status = lines[1].strip().lower()
        return status == "enabled"
    except subprocess.CalledProcessError:
        print("Failed to check System Restore status.")
        return False

def enable_system_restore():
    try:
        subprocess.check_call(["wmic", "restore", "set", "disable=0"])
        print("System Restore has been enabled.")
    except subprocess.CalledProcessError:
        print("Failed to enable System Restore.")

def create_restore_point():
    try:
        subprocess.check_call(["wmic", "recoveros", "set", "createsnapshot"])
        print("System Restore Point created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create System Restore Point.")

def print_welcome_message():
    print("Welcome to Windows Tweaking Program!")

    if not is_system_restore_enabled():
        print("Warning: System Restore is currently disabled.")
        choice = input("Do you want to enable System Restore? (y/n): ").lower()
        if choice == 'y':
            enable_system_restore()
            print()

    input("Press Enter to create a System Restore Point...")
    create_restore_point()
    print("System Restore Point created.")

if __name__ == "__main__":
    print_welcome_message()

    # After the System Restore Point is created, proceed to the menu
    import menu
