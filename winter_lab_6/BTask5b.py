import datetime


def calculate_age(year, month, date):
    date_of_birth = datetime.datetime(year, month, date)
    years = datetime.date.today().year - date_of_birth.year
    days_until_bday = (datetime.datetime.now() - date_of_birth.replace(year=datetime.datetime.now().year)).days
    age = years if days_until_bday>= 0 else years -1
    return age, -days_until_bday

print(calculate_age(1994, 1, 26))