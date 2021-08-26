import names
import random
import datetime
import random_address


def generate():
    gender = ''
    address = random_address.real_random_address()
    gender = ['female', 'male']

    gen = random.choice(gender)
    if gen == 'male':
        gender = 'M'
    else:
        gender = 'F'

    for i in range(1):
        name = names.get_full_name(gen)

    start_date = datetime.date(1900, 1, 1)
    end_date = datetime.date(2021, 8, 25)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    dob = random_date.strftime("%d/%m/%Y")
    md = random_date.strftime("%m%d")

    ph_no = []

    for i in range(0, 8):
        ph_no.append(random.randint(0, 9))

    phone = ''

    for i in ph_no:
        phonedigit = str(i)
        phone = phone + phonedigit

    namestr = name.split()

    info = {'name': name,
            'gender': gender,
            'dateOfBirth': dob,
            'phoneNumber': phone,
            'email': namestr[0] + md + '@gmail.com',
            'address': address['address1'] + ' ' + address['address2'] + ', ' + address['city'] + ', ' + address[
                'state']
            }
    print(info)


generate()


