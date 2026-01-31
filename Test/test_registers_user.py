from data import user
from data.user import User
from pages.registration_page import RegistrationPage


user = User(
    'Таисия',
    'Повали',
    'user@mail.ru',
    'Female',
    '1234567890',
    '1990',
    'March',
    '10',
    'Commerce',
    'Music',
    'cat.jpg',
    'Москва, ул. Ленина, д. 1',
    'Haryana',
    'Karnal'
)

def test_registers_user():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_registration_form(user)
    registration_page.submit()
    registration_page.should_have_registered_user_with()

