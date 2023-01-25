# A Graage Full of Classy Vehicles.
class Vehicle: # Base Class
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 # Full tank of gas
    def drive(self):
        if self.gas >0:
            self.gas-=1
            print('The {} {} goes VROOOOM!'.format(self.color, self.manuf))
        else:
            print('The {} {} sputters out of gas'.format(self.color, self.manuf))
class Car(Vehicle): # Inherits from Vehicle class
    # Turn the radio on:
    def radio(self):
        print("Rockin' Tunes!")
    # Open the window:
    def window(self):
        print('Ahhh ... fresh air!')
class Motorcycle(Vehicle): # Inherits from Vehicle class
    # Puts on motorcycle hemlet:
    def hemlet(self):
        print('Nice and Safe !')
class ElectricCars(Car):
        def drive(self):
            print('The {} {} goes Sheeeeeeeeeeeeeeeeeeee!'.format(self.color, self.manuf))

        
my_car = Car('red', 'Mercedes')
my_car.drive()
my_mc = Motorcycle('silver','Harley')
my_mc.drive()
my_car.radio()
my_car.window()
my_mc.hemlet()
my_ecar = ElectricCars('white','Tesla')
my_ecar.radio()
my_ecar.window()
my_ecar.drive()
my_ecar.gas

