import hashlib
filename = input("import file name:")
try:
    with open(filename, "rb") as file:
        data = file.read()
    md5 = hashlib.md5(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    print("\n========== Encrypting the file =========")
    print("MD5: ", md5)
    print("SHA1: ",sha1)
    print("SHA256:",sha256)
except FileNotFoundError:
    print("file not found on errors:")
    
    

# encryption  file found
from cryptography.fernet import Fernet  
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)
filename = input("Enter file path to encrypt:")
try:
    with open(filename, "rb") as file:
        file_data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print(f"File successfully encrypted and saved as {filename}.enc")
    print("Encryption Key saved to secret.key")

except FileNotFoundError:
    print("Error: Specified file not found.")


# decrypted key
from cryptography.fernet import Fernet

# 1. Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)
filename = input("Enter encrypted file path (.enc): ")

try:
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    # 2. Decrypt the file data
    decrypted_data = fernet.decrypt(encrypted_data)

    # 3. Save the restored file
    output_filename = filename.replace(".enc", "_restored.txt")
    with open(output_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"File decrypted successfully as {output_filename}")

except Exception as e:
    print("Decryption failed:", e)
    
# text hash  Generator
import hashlib
text = input("Enter the text:")
message = input("Enter the message:")
sha512 = hashlib.sha512(text.encode()).hexdigest()
sha256 = hashlib.sha256(text.encode()).hexdigest()
print("SHA-256:", sha256)
print("SHA512:", sha512)


# cracking in a python
import hashlib
target_hash = input("Enter the secret key:")
wordlist = ["admin", "password", "hello world in python"]
for word in wordlist:
    word_hash = hashlib.sha256(word.encode()).hexdigest()
    if word_hash == target_hash:
        print(f"match found:")
        break
    else:
        print("decrypting the message:")