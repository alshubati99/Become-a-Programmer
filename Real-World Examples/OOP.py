# String Objects in python
print('Shirt')
print(type('shirt'))
print(dir('shirt'))
print('shirt'.upper()) 
print(id('shirt'))

# init method: python constructor method for creating new objects; custom __init__ can define unique parameteres for a new object. 
# Python automatically passes an object to the method, so self provides a convient way to access and modify an object within a method. 

# Create a class
class jeans:
    def __init__(self, waist, length, color):
        self.waist= waist
        self.length= length
        self.color=color
        self.wearing = False
    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True
    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearning = False

my_jeans = jeans(31, 33, 'yellow')
print(type(my_jeans))
print(dir(jeans))
my_jeans.put_on()
my_jeans.take_off()

class shirt:
    def __init__(self):
        self.clean = True
    def make_dirty(self):
        self.clean = False
    def make_clean(self):
        self.clean = True

red = shirt()
crimson = red
id(red)
id(crimson)
red.clean
crimson.clean
red.make_dirty()
red.clean
red is crimson
crimson = shirt()
id(crimson)
crimson.clean

# Mutible and immutable items:
closet = ['shirt', 'hat', 'dress', 'pants']
print(closet)
print(id(closet))
print(closet.remove('hat'))



