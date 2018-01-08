from random import randint


### NOTE: Birthday format used dd/mm/yyyy

def generate_random_birthdate():
    date = str(randint(1, 30))
    month = str(randint(1, 12))
    birthdate = str(date + '/' + month)
    return birthdate



def generate_random_birthdays(count):
    birthday_list = []
    while count > 0:
        birthday_list.append(generate_random_birthdate())
        count -= 1
    return birthday_list


birthdates_record = generate_random_birthdays(23)
print('----Birthdays----')
print(birthdates_record)

number_of_duplicates = len(birthdates_record) - len(set(birthdates_record))

print("Number of duplicate birthdays: ", number_of_duplicates)
print("Probability:", number_of_duplicates / 23)