from datetime import datetime
print("Hello I am jarvis")
name=input("What is your name?:")
print(f"Nice to meet you {name}! How can I help you today?")

while True:
     prompt = input('How may i help you?')
     match prompt.lower():
          case "time":
                  now = datetime.now()
                  current_time=now.strftime("%H:%M:%S")
                  print(f"current time is {current_time}")
          case "help":
                 print("What you need to help?")
          case "goodbye":
                 quit()       
         
     