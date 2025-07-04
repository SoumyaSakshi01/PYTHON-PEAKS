import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Create pools of characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the pool
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("🔐 Your generated password is:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

