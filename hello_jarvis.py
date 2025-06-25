from datetime import datetime
print("Hello I am jarvis")
name=input("What is your name?:")
print(f"Nice to meet you {name}! How can I help you today?")

while True:
     prompt = input('How may i help you?')
     if(prompt.lower()=="time"):
          now = datetime.now()
          current_time=now.strftime("%H:%M:%S")
          print(f"current time is {current_time}")

     if(prompt.lower()=="quit"):
          break