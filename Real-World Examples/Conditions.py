diet_restrict=set(['meat', 'cheese'])

if 'meat' in diet_restrict:
    print('Get a cheese pizza')
elif 'meat' and 'cheese' in diet_restrict:
    print('Get a vegan pizza')
else:
    print('Get something else')
# Each expression is a boolean value. 
diet_restrict=set(['meat', 'cheese'])
if 'meat' and 'cheese' in diet_restrict:
    print('Get a vegan pizza')
elif 'meat' in diet_restrict:
    print('Get a cheese pizza')
else:
    print('Get something else')
#########################
Today = 'Saturday'
if Today is 'Sun':
    print('Spinach Pizza')
elif Today is 'Mon':
    print('Mushroom Pizza')
elif Today is 'Mon':
    print('Mushroom Pizza')
elif Today is 'Tue':
    print('Pepperoni Pizza')
elif Today is 'Wed':
    print('Veggie Pizza')
elif Today is 'Thur':
    print('Bbq Pizza')
elif Today is 'Fri':
    print('Sausage Pizza')
elif Today is 'Saturday':
    print('Hawaiian Pizza')
# Write the previous code differently:
specials = {
    'Sun': 'Spinach',
    'Sat': 'Mushroom',
    'Mon': 'Pepperoni',
    'Tue': 'Veggie',
    'Wed': 'Bbq chicken',
    'Thur': 'Sausage',
    'Fri': 'Hawaiian',
}
def order(day):
    pizza = specials [day]
    print('order the {} pizza. '.format(pizza))
order('Fri')