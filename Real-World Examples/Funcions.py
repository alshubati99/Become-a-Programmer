# Make Functions:
def cook():
    print("mix ingredients")
    print("Pour mixture into frying pan")
    print("cook first side")
    print("flipp it")
    print("cook the other side")
def make_omelette():
    cook()
    omelette = " Tasty omelette "
    return omelette
omelette1 = make_omelette()
print(omelette1)
def make_pancake():
    cook()
    pancake = " Tasty pancake! "
    return pancake
pancake1 = make_pancake()
print(pancake1)

# Make Functions with Input/ Parameters:
def cook():
    print("mix ingredients")
    print("Pour mixture into frying pan")
    print("cook first side")
    print("flipp it")
    print("cook the other side")
def make_omelette(ingredient):
    cook()
    omelette = 'a {}  omelette '.format(ingredient)
    return omelette
omelette1 = make_omelette('cheese')
print(omelette1)
def make_pancake():
    cook()
    pancake = " Tasty pancake! "
    return pancake
pancake1 = make_pancake()
print(pancake1)

# * to tell python to expect any number of arguments when function is called.
# ingredient is a local variable 
# local comes before global. 
def fancy_omelette(*ingredients):
    cook()
    make_omelette()
    omelette8 = 'a fancy omelette with {} ingredients'.format(len(ingredients))
    return omelette8

omelette3 = fancy_omelette('cheese', 'onion', 'tomatoes')

