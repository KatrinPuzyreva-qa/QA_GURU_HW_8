import datetime
from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, first_name='Таисия', last_name='Повали', email='user@mail.ru',
                 gender='Female', mobile_number='1234567890', birth_year='1990', birth_month='March',
                 birth_day='10', subject='Commerce', hobbies='Music', picture = 'cat.jpg', address='Москва, ул. Ленина, д. 1',
                 state='Haryana', city='Karnal'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile_number = mobile_number
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.subject = subject
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
        self.state = state
        self.city = city


