#Exercise 1 : Cars
def replace_spaces(item):
    return item.strip()
manufacturers = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(',')
manufacturers = list(map(replace_spaces, manufacturers))
print(f'There are {len(manufacturers)} companies in the brands list.')
print(manufacturers [::-1])
manufacturers_with_o_count = len([brand for brand in manufacturers if 'o' in brand.lower()])
manufacturers_without_i_count = len([brand for brand in manufacturers if 'i' not in brand.lower()])
print(f'There are {manufacturers_with_o_count} manufacturers with an "o" and {manufacturers_without_i_count} manufacturers witout "i".'.format())

#6
manufacturers = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
manufacturers = set(manufacturers)
print(*manufacturers, sep=',')
print(len(manufacturers))
manufacturers = list(set(manufacturers))


#7
for item in manufacturers:
    print(item[::-1])

