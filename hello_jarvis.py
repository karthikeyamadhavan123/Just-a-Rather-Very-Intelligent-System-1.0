import logging
from datetime import datetime

logging.basicConfig(filename='jarvis.log',
                    format='%(asctime)s:%(message)s', level=logging.DEBUG, filemode='a')


def start_jarvis():
    return "Hello I am jarvis"


def greet_name_user(name):
    return f"Nice to meet you {name}! How can I help you today?"


def timedisplay():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"current time is {current_time}"


def helpuser():
    try:
        with open('help.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError as e:
        logging.debug(e)
        return e


def take_prompt(prompt):
    match prompt.lower().strip():
        case "time":
            return timedisplay()
        case "help":
            return helpuser()
        case "goodbye":
            write_into_file(
                "J.A.R.V.I.S. replied with goodbye sir! Have a nice day ")
            logging.debug("User ended the session with 'goodbye' command.")
            print("Goodbye sir! Have a nice day.")
            quit()
        case _:
            return "Sorry, I didn't understand that command."


def write_into_file(content):
    try:
        now =datetime.now()
        date=now.date()
        with open("history.txt", "a", encoding='utf-8') as f:
            f.write("\n")
            f.write(str(date) +  " " + content)
    except Exception as e:
        print(e)
        logging.debug(e)


def main():
    start = start_jarvis()
    print(start)
    logging.debug(start)
    name = input("What is your name? ")
    write_into_file(content=f"User entered his name {name}")
    greet_msg = greet_name_user(name)
    print(greet_msg)
    write_into_file(content=f"J.A.R.V.I.S. replied with {greet_msg}")
    logging.debug(greet_msg)
    while True:
        prompt = input("How may I help you? ")
        write_into_file(f"User has demanded with this prompt {prompt}")
        response = take_prompt(prompt)
        if response:
            write_into_file(f"J.A.R.V.I.S. replied with {response}")
            print(response)
            logging.debug(response)


if __name__ == "__main__":
    main()
