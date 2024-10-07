
# Windows Tweaker
This is a documentation of this project.
---
![GitHub repo size](https://img.shields.io/github/repo-size/ritaban06/Windows_tweaker)


This code is in python programming language.

This documentation contains document of each file created in the project folder.

## 1. Welcome.py

## a) Purpose

The script provides a welcome message, checks the status of System Restore, gives the option to enable System Restore if it's disabled, creates a System Restore Point, and then presents a menu for selecting different feature sets. The user can choose between all
features, features specific to Windows 11, or exit the program.

## b) Functions

The script contains several functions to handle different tasks:

i) is_system_restore_enabled():

Purpose: This function checks if System Restore is enabled on the Windows system.

Input: None

Output: Returns a boolean value (True if System Restore is enabled, False otherwise).

Description: The function uses the subprocess module to run the "wmic restore get disablestatus" command, which retrieves the status of  System Restore. It then parses the output to determine whether System Restore is enabled or not.

ii) enable_system_restore():

Purpose: This function enables System Restore on the Windows system.

Input: None

Output: None

Description: The function uses the subprocess module to run the "wmic restore set disable=0" command, which enables System Restore.

iii) create_restore_point():

Purpose: This function creates a System Restore Point on the Windows system.

Input: None

Output: None

Description: The function uses the subprocess module to run the "wmic recoveros set createsnapshot" command, which creates a System
Restore Point.

iv) print_welcome_message():

Purpose: This function displays the welcome message and initiates the program flow.

Input: None

Output: None

Description: The function checks the status of System Restore using is_system_restore_enabled(). If System Restore is disabled, it asks the user whether to enable it or not. After the user's input, it creates a System Restore Point and displays a message confirming its creation.

## c) Main Program Flow

The main program flow is controlled within the if __name__ == __main__: block.

The print_welcome_message() function is called to display the welcome message and check System Restore status. After the System Restore 
Point is created, the program enters a loop to display the main menu repeatedly until the user decides to exit. The user is prompted to 
select a menu option (1, 2, or 3). If the user selects option 1, it imports and executes the all_features_menu.py module. If the user 
selects option 2, it imports and executes the windows_11_features_menu.py module. If the user selects option 3, the program prints 
"Exiting..." and breaks out of the loop, ending the program. If the user enters an invalid choice, it displays an error message, and the
loop repeats.
