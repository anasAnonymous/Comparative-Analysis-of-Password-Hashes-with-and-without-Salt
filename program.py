import hashlib
import os
import time


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_salt():
    return os.urandom(16)

def salt_hash(password, salt):
    return hashlib.sha256(password.encode()+salt).hexdigest()


def save_credentials(credentials_file, username, password_hash, salt_hash_var):

    """Saves username and hashed password with and without salt to a text file."""
    with open(credentials_file, "a") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password hash: {password_hash}\n")
        file.write(f"Salted Hash: {salt_hash_var}\n\n")

    time.sleep(1)
    print("Credentials saved successfully.\n")
    

def read_password_hashes(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                yield line.strip()  # Strips newline characters from each line and yields it
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def crack_password(password_hash, salt_hash_var):
    flag = 0; salt_flag = 0
    common_password_file = "password_hashes.txt"
    """
    current passwords and their SHA-256 hashes that I have stored in this file are:
        hash : password
        5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 : password
        65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5 : qwerty
        8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92 : 123456
        1df38cbe202365fc6f2265391ef6aad4e52c7c09ce837bd191e4081b8749e341 : anas
    """
    for line in read_password_hashes(common_password_file):
        #print(line)
        #print(password_hash)
        if password_hash == line:
            flag = 1
            break
        if salt_hash_var == line:
            salt_flag == 1
            break
    
    time.sleep(1)
    print("Checking if your password found in our dictionary of common passwords.....")
    time.sleep(1)
    if flag == 1:
        print(f"WARNING: Your password is weak and found in our dictionary of common passwords! \nHash: {password_hash}\n")        
    else:
        print("Your password seems strong.")

    time.sleep(1)
    print("Checking if your password with the salt can be found in our dictionary of common passwords.....")
    time.sleep(1)
    if salt_flag == 1:
        print(f"WARNING: Even after adding salt, your password got cracked! \nSalted Hash: {salt_hash_var}")        
    else:
        print("Not a joke to crack a hash with salt! Right?")


def main():
    print("Welcome! Please enter your credentials.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hash_without_salt = hash_password(password)
    salt = generate_salt()
    hash_with_salt = salt_hash(password, salt)
    credentials_file = "credentials.txt"

    save_credentials(credentials_file, username, hash_without_salt, hash_with_salt)

    crack_password(hash_without_salt, hash_with_salt)
    

if __name__ == "__main__":
    main()
