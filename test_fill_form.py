import os
from selene import browser, have



class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")


    def fill_first_name(self, value):
        browser.element('#firstName').type(value)


    def fill_last_name(self, value):
        browser.element('#lastName').type(value)


    def fill_email(self, value):
        browser.element('#userEmail').type(value)


    def fill_gender(self, gender):
        browser.element('[for="gender-radio-2"]').click()


    def fill_mobile_number(self, mobile_number):
        browser.element('#userNumber').type(mobile_number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()

        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select') \
            .all('option') \
            .element_by(have.text(year)) \
            .click()

        # Выбираем месяц
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select') \
            .all('option') \
            .element_by(have.text(month)) \
            .click()

        # Выбираем день
        browser.element(f'.react-datepicker__day--{day}').click()


    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject)
        browser.element('.subjects-auto-complete__menu').element('div').click()


    def fill_hobbies(self, hobbies):
        browser.element('[for="hobbies-checkbox-3"]').click()


    def upload_picture(self):
        browser.element('#uploadPicture').set_value(os.path.abspath('cat.jpg'))


    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)


    def fill_state(cls, state):
        browser.element('#react-select-3-input').type(state)
        browser.element('[id^="react-select-3-option-"]').click()


    def fill_city(cls, city):
        browser.element('#react-select-4-input').type(city)
        browser.element('[id^="react-select-4-option-"]').click()


    def submit(self):
        browser.element('#submit').click()

    def should_have_submission_confirmation(self, text):
        browser.element('.modal-content').should(have.text(text))

    def should_have_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                                         subject, hobbies, file, address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subject,
                hobbies,
                file,
                address,
                city
            )
        )





def test_fill_form():

    registration_page = RegistrationPage
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
    registration_page.should_have_submission_confirmation('Thanks for submitting the form')

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

