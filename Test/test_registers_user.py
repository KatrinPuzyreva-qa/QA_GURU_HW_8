from pages.registration_page import RegistrationPage
from data.users import Users

user = Users(
    'Таисия Повали',
    'user@mail.ru',
    'Female',
    '9991234567',
    '10 March,1990',
    'Commerce',
    'Music',
    'cat.jpg',
    'Москва, ул. Ленина, д. 1',
    'Haryana Karnal'
)

def test_registers_user():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_registration_form(user)
    registration_page.submit()
    registration_page.should_have_submitted()
