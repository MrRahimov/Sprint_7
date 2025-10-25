import random
import string

def rand_str(n=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def build_courier(login=None, password=None, first_name=None):
    return {
        "login": login or rand_str(),
        "password": password or rand_str(),
        "firstName": first_name or rand_str(),
    }

def build_order(colors=None):
    return {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, Тверская 1",
        "metroStation": 5,
        "phone": "+7 999 111 22 33",
        "rentTime": 5,
        "deliveryDate": "2025-12-01",
        "comment": "Автотест",
        "color": colors if colors is not None else [],
    }
