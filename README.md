# Comparative Analysis of Password Hashes with and without Salt


## Overview

This Python program allows users to register their credentials securely, including their username and password. It utilizes hashing techniques for password storage, along with the addition of salt for enhanced security. The program also includes functionality to check if the user's password can be guessed or not both with and without salt.


## Functions

### `hash_password(password)`

- **Purpose**: Hashes the given password using the SHA-256 hashing algorithm.
- **Parameters**: 
  - `password`: The password to be hashed.
- **Returns**: 
  - The hashed password.

### `generate_salt()`

- **Purpose**: Generates a random salt for salting the password.
- **Returns**: 
  - A randomly generated salt.

### `salt_hash(password, salt)`

- **Purpose**: Computes the salted hash of the given password.
- **Parameters**: 
  - `password`: The password to be hashed.
  - `salt`: The salt to be added to the password before hashing.
- **Returns**: 
  - The salted hash of the password.

### `save_credentials(credentials_file, username, password_hash, salt_hash_var)`

- **Purpose**: Saves the user's credentials to a text file, including their username, hashed password (without salt), and salted hash of the password.
- **Parameters**: 
  - `credentials_file`: The file to which the credentials will be saved.
  - `username`: The username of the user.
  - `password_hash`: The hashed password without salt.
  - `salt_hash_var`: The salted hash of the password.
- **Returns**: 
  - None.

### `read_password_hashes(filename)`

- **Purpose**: Reads the common password hashes from a file line by line.
- **Parameters**: 
  - `filename`: The name of the file containing the common password hashes.
- **Yields**: 
  - Each line (password hash) from the file.

### `crack_password(password_hash, salt_hash_var)`

- **Purpose**: Checks if the user's password is present in the dictionary of common passwords, both with and without salt.
- **Parameters**: 
  - `password_hash`: The hashed password without salt.
  - `salt_hash_var`: The salted hash of the password.
- **Returns**: 
  - None.

### `main()`

- **Purpose**: The main function that orchestrates the registration process, saving credentials, and checking password security.
- **Parameters**: 
  - None.
- **Returns**: 
  - None.

## Usage

1. Execute the program.
2. Provide a username and password when prompted.
3. The program will save the credentials securely and check if the password is present in the dictionary of common passwords, both with and without salt.
4. The user will be notified about the strength of their password and whether it was found in the common password dictionary.

---

