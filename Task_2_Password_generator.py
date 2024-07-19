import random
import string

def generate_password(length):
    #This function generates a random password.
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("\nWelcome to the Password Generator!")

while True:
    #take input from the user for password length.
    length = int(input("Enter the desired password length:"))

    if length <= 0:
        raise ValueError("Password lenght must be greater than zero")
    
    #Displaying the password
    password = generate_password(length)
    print(f"\nGenerated password:{password}\n")