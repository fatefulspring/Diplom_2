import random
import string


def generate_registration_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(10)}@{generate_random_string(3)}.{generate_random_string(3)}'
    password = generate_random_string(10)
    name = generate_random_string(10)


    return email, password, name

