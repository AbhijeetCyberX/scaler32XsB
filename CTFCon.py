correct_flag = "CTF{python_is_fun}"
user_input = input("Enter the flag:")
if user_input == correct_flag:
    print("Correct! You have found the flag.")
else:
    print("Incorrect flag. Try again.")

#base 64 decoder with python
import base64
data = input("Enter the base64 encoded string: ")
decoded = base64.b64decode(data).decode()
print("Decoded string:", decoded)
            
# brute force professional
correct_password = "password1234"
password = [
    "admin",
    "password1234",
    "password",
    "hello world",
    "MIT @# 115072",
    "admin less"
]
for password in password:
    print("trying a password working")
    
    if password == correct_password:
        print("password found:",password)
        break
    
import os
folder = "challenge"
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
         with open(filepath, "r", errors="ignore") as file:
            data = file.read()

            if "CTF{" in data:
                print("Possible flag found:", filename)