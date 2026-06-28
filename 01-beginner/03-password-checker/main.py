import re
import random
import string
import sys


def Checker():
    password = str(input("Enter your password:  "))
    point = 0

    if len(password) >= 8 and len(password) <= 12:
        point += 1
    if re.search(r"[A-Z]", password):
        point += 1
    if re.search(r"[a-z]", password):
        point += 1
    if re.search(r"[0-9]", password):
        point += 1
    if re.search(r"[^a-zA-Z0-9\s]" , password):
        point += 1

   
    if point >= 0 and point <= 2:
      print(f"Your password is weak, with only {point}.")
    elif point == 3 or point == 4:
      print(f"Your password is Medium, with {point}.")
    else:
      print(f"Your password is STRONG!!, with {point}.")


def Generator():
   
    password_length = 0
    password_uppercase = "no"
    password_numbers = "no"
    password_specchara = "no"

    if "--length" in sys.argv:
        try:
            idx = sys.argv.index("--length")
            password_length = int(sys.argv[idx + 1])
        except (ValueError, IndexError):
            pass  

    if "--uppercase" in sys.argv:
        password_uppercase = "yes"
    if "--numbers" in sys.argv:
        password_numbers = "yes"
    if "--spacial" in sys.argv or "--special" in sys.argv:
        password_specchara = "yes"

    
    if not password_length:
        print("You must give me a length for your password.")
        password_length = int(input("Enter the length of the password: "))

    if password_length < 8:
        print("Your password is too short! It must be at least 8 characters.")
        return  
    else:
        print("Password meets the minimum length requirement.")

    
    uppercase = string.ascii_uppercase if password_uppercase == "yes" else ""
    numbers = string.digits if password_numbers == "yes" else ""
    specialchar = string.punctuation if password_specchara == "yes" else ""
    lower = string.ascii_lowercase  

    
    guaranteed = []

    if uppercase:
        guaranteed.extend(random.choices(uppercase, k=3))
    if numbers:
        guaranteed.extend(random.choices(numbers, k=2))
    if specialchar:
        guaranteed.extend(random.choices(specialchar, k=2))

    
    remaining_length = password_length - len(guaranteed)
    if remaining_length > 0:
        guaranteed.extend(random.choices(lower, k=remaining_length))

    
    random.shuffle(guaranteed)
    password = "".join(guaranteed)

    print(f"Generated Password: {password}")


    

check_generate = int(input("Do you want to check your password or to generate a new ? (to check reply 1 , to genrate reply 2)"))


if check_generate == 1 and len(sys.argv) < 2:
    Checker()

elif check_generate == 2 and len(sys.argv) > 1:
    Generator()

elif check_generate == 2:
    Generator()

else:
    print("Invalid input")

      
      
    
   



