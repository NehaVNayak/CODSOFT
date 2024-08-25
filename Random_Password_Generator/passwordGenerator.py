#Random Password Generator
import random
import string

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Get user input for the password length
length = int(input("Enter the desired password length: "))

# Generate the password
password = generate_password(length)

# Display the generated password
print(f"Generated Password: {password}")
