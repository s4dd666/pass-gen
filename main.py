import random
import string

def generate_password(length, uppercase=True, lowercase=True, symbols=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if symbols:
        characters += string.punctuation
    if not characters:
        characters = string.digits
    else:
        characters += string.digits

    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    length = int(input("Укажите длину пароля: "))
    use_uppercase = input("Включить использование заглавных букв? (y/n): ").lower() == "y"
    use_lowercase = input("Включить использование строчных букв? (y/n): ").lower() == "y"
    use_symbols = input("Включить использование специальных символов? (y/n): ").lower() == "y"

    password = generate_password(length=length, uppercase=use_uppercase, lowercase=use_lowercase, symbols=use_symbols)
    print("Пароль сгенерирован:")
    print(password)

    generate_another = input("Хотите сгенерировать еще один пароль? (y/n): ").lower() == "y"
    if not generate_another:
        print("Генерация паролей завершена")
        break
