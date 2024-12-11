import string
import random

char = string.ascii_letters+string.digits+string.punctuation

password = " ".join(random.choices(char,k=18))

print(password)