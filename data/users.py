from dataclasses import dataclass

@dataclass
class User:
    first_name: str = 'Таисия'
    last_name: str = 'Повали'
    email: str = 'user@mail.ru'
    gender: str = 'Female'
    mobile_number: str = '1234567890'
    birth_year: str = '1990'
    birth_month: str = 'March'
    birth_day: str = '10'
    subject: str = 'Commerce'
    hobbies: str = 'Music'
    picture: str = 'cat.jpg'
    address: str = 'Москва, ул. Ленина, д. 1'
    state: str = 'Haryana'
    city: str = 'Karnal'

