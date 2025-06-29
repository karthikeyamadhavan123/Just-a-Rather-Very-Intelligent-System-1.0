# Import required modules for logging and date/time functionality
import logging
from datetime import datetime

# Configure logging to save all debug messages to jarvis.log file
# 'a' mode means append - new logs will be added to existing file
logging.basicConfig(filename='jarvis.log',
                    format='%(asctime)s:%(message)s', 
                    level=logging.DEBUG, 
                    filemode='a')

def start_jarvis():
    """
    Initialize Jarvis with a welcome message.
    
    Returns:
        str: Welcome message for the user
    """
    return "Hello I am jarvis"

def greet_name_user(name):
    """
    Create a personalized greeting for the user.
    
    Args:
        name (str): User's name
        
    Returns:
        str: Personalized greeting message
    """
    return f"Nice to meet you {name}! How can I help you today?"

def timedisplay():
    """
    Get the current time and format it for display.
    
    Returns:
        str: Current time in HH:MM:SS format
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"current time is {current_time}"

def helpuser():
    """
    Read and return help information from help.txt file.
    
    Returns:
        str: Contents of help.txt file or error message if file not found
    """
    try:
        # Try to open and read the help file
        with open('help.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError as e:
        # Log the error and return the exception (user will see technical error)
        logging.debug(e)
        return e

def take_prompt(prompt):
    """
    Process user commands and return appropriate responses.
    
    Args:
        prompt (str): User's command input
        
    Returns:
        str: Response based on the command, or error message for unknown commands
    """
    # Convert to lowercase and remove whitespace for consistent matching
    match prompt.lower().strip():
        case "time":
            # User wants to know current time
            return timedisplay()
        case "help":
            # User needs help information
            return helpuser()
        case "goodbye":
            # User wants to end the session
            write_into_file("J.A.R.V.I.S. replied with goodbye sir! Have a nice day ")
            logging.debug("User ended the session with 'goodbye' command.")
            print("Goodbye sir! Have a nice day.")
            quit()  # Exit the program
        case _:
            # Default case - command not recognized
            return "Sorry, I didn't understand that command."

def write_into_file(content):
    """
    Write interaction history to history.txt file with timestamp.
    
    Args:
        content (str): The content to write to the history file
    """
    try:
        # Get current date for timestamping
        now = datetime.now()
        date = now.date()
        
        # Append to history file (creates file if it doesn't exist)
        with open("history.txt", "a", encoding='utf-8') as f:
            f.write("\n")  # Add newline for readability
            f.write(str(date) + " " + content)  # Write date + content
    except Exception as e:
        # Print and log any errors that occur during file writing
        print(e)
        logging.debug(e)

def main():
    """
    Main program loop - handles initialization and user interaction.
    """
    # Initialize Jarvis and display welcome message
    start = start_jarvis()
    print(start)
    logging.debug(start)  # Log the startup message
    
    # Get user's name and create personalized greeting
    name = input("What is your name? ")
    write_into_file(content=f"User entered his name {name}")  # Log name entry
    
    greet_msg = greet_name_user(name)
    print(greet_msg)
    write_into_file(content=f"J.A.R.V.I.S. replied with {greet_msg}")  # Log greeting
    logging.debug(greet_msg)
    
    # Main interaction loop - continues until user says "goodbye"
    while True:
        # Get user command
        prompt = input("How may I help you? ")
        write_into_file(f"User has demanded with this prompt {prompt}")  # Log user input
        
        # Process the command and get response
        response = take_prompt(prompt)
        
        # If there's a response (should always be true), display and log it
        if response:
            write_into_file(f"J.A.R.V.I.S. replied with {response}")  # Log response
            print(response)  # Display response to user
            logging.debug(response)  # Log response to debug file

# Standard Python idiom - only run main() if this file is executed directly
# (not imported as a module)
if __name__ == "__main__":
    main()