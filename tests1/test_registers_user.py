from data.users import User
from pages.registration_page import RegistrationPage


user = User(
    first_name='Таисия',
    last_name='Повали',
    email='user@mail.ru',
    gender='Female',
    mobile_number='1234567890',
    birth_year='1990',
    birth_month='March',
    birth_day='10',
    subject='Commerce',
    hobbies='Music',
    picture='cat.jpg',
    address='Москва, ул. Ленина, д. 1',
    state='Haryana',
    city='Karnal'
)

def test_registers_user():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_registration_form(user)
    registration_page.submit()
    registration_page.should_have_registered_user_with(user)

