import string
import random

def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

lengte =int(input("Wat is je gewenste wachtwoord lengte?: "))

print(password_generator(lengte))
