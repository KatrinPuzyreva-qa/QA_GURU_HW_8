from tests.registration_page import RegistrationPage


def test_fill_form():

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name('Таисия')
    registration_page.fill_last_name('Повали')
    registration_page.fill_email('user@mail.ru')
    registration_page.fill_gender('Female')
    registration_page.fill_mobile_number('9991234567')
    registration_page.fill_date_of_birth('1990', 'March', '10')
    registration_page.fill_subjects('Commerce')
    registration_page.fill_hobbies('Music')
    registration_page.upload_picture()
    registration_page.fill_current_address('Москва, ул. Ленина, д. 1')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')
    registration_page.submit()
    registration_page.should_have_registered_user_with(
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

