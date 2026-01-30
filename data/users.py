import datetime
from dataclasses import dataclass


@dataclass
class Users:
    full_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: datetime.date
    subject: str
    hobbies: str
    file: str
    address: str
    city: str


