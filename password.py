import random
import string
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
pass_length = int(input("password length: "))
print("Password:", generate_password(pass_length))