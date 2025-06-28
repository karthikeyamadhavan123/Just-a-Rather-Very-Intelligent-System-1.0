from datetime import datetime

def start_jarvis():
        print("Hello I am jarvis")

def greet_name_user(name):
       print(f"Nice to meet you {name}! How can I help you today?") 

def timedisplay():
       now = datetime.now()
       current_time=now.strftime("%H:%M:%S")
       print(f"current time is {current_time}")

def helpuser():
       try:
           with open('help.txt','r',encoding='utf-8') as f:
                 print(f.read())
       except FileNotFoundError as e:
             print(e)

def take_prompt(prompt):
      match prompt.lower():
          case "time":
                  timedisplay()
          case "help":
                 helpuser()
          case "goodbye":
                 quit()   
          case _:
            print("Sorry, I didn't understand that command.")

def main():
    start_jarvis()
    name = input("What is your name? ")
    greet_name_user(name)

    while True:
        prompt = input("How may I help you? ")
        take_prompt(prompt)

if __name__ == "__main__":
    main()