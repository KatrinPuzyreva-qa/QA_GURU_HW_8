import os
from selene import browser, be
from selene.support.conditions import have


class RegistrationPage:
    def __init__(self):
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')

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
        radio_id = {"Male": 1, "Female": 2}.get(gender)
        browser.element(f'[for="gender-radio-{radio_id}"]').click()

    def fill_mobile_number(self, mobile_number):
        browser.element('#userNumber').type(mobile_number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()

        self.year.click()
        self.year \
            .all('option') \
            .element_by(have.text(year)) \
            .click()

        # Выбираем месяц
        self.month.click()
        self.month \
            .all('option') \
            .element_by(have.text(month)) \
            .click()

        # Выбираем день
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject)
        browser.element('.subjects-auto-complete__menu').element('div').click()

    def fill_hobbies(self, hobbies):
        hobby_map = {"Sports": 1, "Reading": 2, "Music": 3}
        for hobby in hobbies.split(','):
            hobby_id = hobby_map[hobby.strip()]
            browser.element(f'[for="hobbies-checkbox-{hobby_id}"]').click()

    def upload_picture(self):
        browser.element('#uploadPicture').set_value(os.path.abspath('cat.jpg'))

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').click()

    def should_have_submission_confirmation(self):
        browser.element('.modal-content').should(have.text('Thanks for submitting the form'))


    def should_have_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                                         subject, hobbies, file, address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(full_name, email, gender, mobile_number, date_of_birth, subject, hobbies, file, address, city)
        )

    def fill_registration_form(self, user):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_gender(user.gender)
        self.fill_mobile_number(user.mobile_number)
        self.fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)
        self.fill_subjects(user.subject)
        self.fill_hobbies(user.hobbies)
        self.upload_picture()
        self.fill_current_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit()
