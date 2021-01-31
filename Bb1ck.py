# Bb1ck learn greeting in all language with your phone or computer whitooth going to school...

def morning():
     print("Bonjour ! ")
     print(f"""\ Explainations:
At {time}am in france and all country that they talk in french,\n the greet expression is:\n Bonjour that mean Good morning """)



def evening():
      print("Bonsoir !")
      print(f"""\n\n Explainations:
At {time}pm in france and all country that they talk in french,\n the greet expression is:\n Bonsoir that mean Good afternoon or Good evening """)


time = int(input("Please enter the time of your own to know how may you greet in french at this time: "))
if time <=12:
   morning()
elif time >= 12:
   evening()
else:
   pass
