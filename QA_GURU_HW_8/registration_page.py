import os
from selene import browser
from selene.support.conditions import have


class RegistrationPage:

    def __init__(self):
        pass

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)


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



