food_list = ['맛나피자','새로피자','대왕햄버거','군대햄버거']

#피자집 개수와, 햄버거집 개수 프린트

pizza = 0
ham = 0

for i in food_list:
    food = i[2:]
    if food == '피자':
        pizza = pizza + 1
    elif food == '햄버거':
        ham = ham + 1
print('피자 가게 개수: ', pizza)
print('햄버거 가게 개수: ', ham)
