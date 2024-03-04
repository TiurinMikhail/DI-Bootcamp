#Exercise 1 : Hello World-I Love Python
print('Hello World\n'*4,'I love Python\n'*4,sep='')

#Exercise 2 : What Is The Season ?
user_month = int(input('Please,input a month (number from 1 to 12): '))
Spring = [3,4,5]
Winter = [12,1,2]
Summer = [6,7,8]
Autumn  = [9,10,11]
if user_month in Spring:
    print('The month is Spring')
elif user_month in Winter:
    print('The month is Winter')
elif user_month in  Summer:
    print('The month is Summer')
elif user_month in Autumn:
    print('The month is Autumn')

#or!!!!
Spring = [3,4,5]
Winter = [12,1,2]
Summer = [6,7,8]
Autumn  = [9,10,11]
list_of_month = [i for i in range(1,13)]
user_month = int(input('Please,input a month (number from 1 to 12): '))
while user_month>1 :
    if user_month not in list_of_month:
        print('The number of month is not correct. Please try again.')
        user_month = int(input('Please,input a month (number from 1 to 12): '))
    else:
        if user_month in Spring:
            print('The month is Spring')
        elif user_month in Winter:
            print('The month is Winter')
        elif user_month in  Summer:
            print('The month is Summer')
        else:
            print('The month is Autumn')
        break

