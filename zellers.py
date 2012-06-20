
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
print 'Enter your date of birth: '
day = input('       Day? ')
month = input('     Month? (March: 1,April: 2, May: 3,June: 4, July: 5,August: 6, Septmber: 7, October: 8,November: 9,December: 10 Jan: 11, Feb: 12) ')
year = input('      Year? (If born in January or Febuary, enter previousyear) ')

century = year/100
year = year % 100


W= (13 * month - 1) / 5
X= year / 4
Y= century / 4
Z= W + X + Y + day + year - 2 * century
R= Z % 7

if R == 0:
    birthday ='Sunday'
elif R == 1:
   birthday ='Monday'
elif R == 2:
    birthday ='Tuesday'
elif R == 3:
    birthday ='Wednesday'
elif R == 4:
   birthday ='Thursday'
elif R == 5:
    birthday ='Friday'
elif R == 6:
    birthday ='Saturday'

print first_name, last_name, 'was born on day', birthday, 'of the week'


