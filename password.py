import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short. Must be at least 4 characters."

    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure a mix of character types
    all_chars = letters + digits + symbols
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length
     password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)  # Shuffle to make it more secure

    return ''.join(password)

# Main program
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
