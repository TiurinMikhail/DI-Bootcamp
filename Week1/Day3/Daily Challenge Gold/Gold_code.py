#Encryption
s = input('Enter a string: ')
const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы
n = int(input('Enter the shift: '))
final_s = ''
for i in range(len(s)):
    if s[i].islower():
        new_position = const_lower_en.find(s[i]) + n
    else:
        new_position = const_upper_en.find(s[i]) + n

    if s[i].isalpha():
        if new_position > 25 and s[i].islower():
            final_s += const_lower_en[new_position-26]
        elif new_position > 25  and s[i].isupper():
            final_s += const_upper_en[new_position-26]
        elif s[i].islower():
            final_s += const_lower_en[new_position]
        elif s[i].isupper():
            final_s += const_upper_en[new_position]
    else:
        final_s += s[i]
print(final_s)

#
print('---------------------\n'*2)
#
#Decription
s = final_s
const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы
final_s = ''
for i in range(len(s)):
    if s[i].islower():
        new_position = const_lower_en.find(s[i]) - n
    else:
        new_position = const_upper_en.find(s[i]) - n

    if s[i].isalpha():
        if new_position < 0 and s[i].islower():
            final_s += const_lower_en[new_position+26]
        elif new_position < 0  and s[i].isupper():
            final_s += const_upper_en[new_position+26]
        elif s[i].islower():
            final_s += const_lower_en[new_position]
        elif s[i].isupper():
            final_s += const_upper_en[new_position]
    else:
        final_s += s[i]
print(final_s)
