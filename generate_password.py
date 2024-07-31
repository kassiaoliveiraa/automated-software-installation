import random
import string

def generate_password(length=12):
    if length < 12:
        raise ValueError("A senha deve ter no mínimo 12 caracteres.")
    
    # Define os caracteres obrigatórios
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%&*")

    # Preenche o restante da senha com caracteres aleatórios
    all_characters = string.ascii_letters + string.digits + "!@#$%&*"
    remaining_length = length - 4
    remaining_characters = random.choices(all_characters, k=remaining_length)

    # Combina todos os caracteres e embaralha a senha
    password_list = list(upper + lower + digit + special + ''.join(remaining_characters))
    random.shuffle(password_list)
    
    return ''.join(password_list)

# Gera uma senha
print(generate_password(12))
