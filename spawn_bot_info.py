import random
import string
import pandas as pd

def generate_random_name():
    first_names = ["John", "Jane", "Robert", "Emily", "Michael", "Sarah", "William", "David", "Christopher", "Jessica"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return (first_name, last_name)

def generate_random_email(first_name, last_name):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(10))
    email = f"{first_name.lower()}.{last_name.lower()}+{random_numbers}@hotmail.com"

    return email

def generate_random_password(length=8):
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for i in range(length))

    return password



def save_to_csv(bot_info, filename):
    df = pd.DataFrame(bot_info)
    df.to_csv(filename, index=False)



def spawn_bot_info(num_bots):
    bot_info_dict = []
    for i in range(num_bots):
        first_name, last_name = generate_random_name()
        email = generate_random_email(first_name, last_name)
        password = generate_random_password()

        bot_info_dict.append({
            "First": first_name,
            "Last": last_name,
            "Email": email,
            "Password": password
        })
    save_to_csv(bot_info_dict,'bot_info.csv')
    


