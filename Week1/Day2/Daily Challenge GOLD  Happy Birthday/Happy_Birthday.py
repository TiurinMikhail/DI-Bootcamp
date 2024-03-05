user_birthday = input('Enter your date of birth ( DD/MM/YYYY): ')

from datetime import datetime

birth_date = datetime.strptime(user_birthday, '%d/%m/%Y')


# Calculating age
def calculate_age(birth_date):
    today = datetime.today()
    cnt_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return cnt_age


age = calculate_age(birth_date)


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True


last_num = int(str(age)[-1])
count_spaces_left = (11-last_num)//2
count_spaces_right = 11-last_num-count_spaces_left
if is_year_leap(birth_date.year):
    for i in range(2):
        print(' '*7, '_'*count_spaces_left, 'i'*last_num, '_'*count_spaces_right, """
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
        """,sep='')

else:
    print(' ' * 7, '_' * count_spaces_left, 'i' * last_num, '_' * count_spaces_right, """
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
    """,sep='')

