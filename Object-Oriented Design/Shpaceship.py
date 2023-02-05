class Spaceship:
    def __init__(self):
    # instance variables:
        self.callSign = ''
        self._shieldStrength = 100
    # Methods:

    def fireMissile(self):
        return "pew!"
    
    def reduceShield(self, amount):
       self.shieldStrength -= amount



