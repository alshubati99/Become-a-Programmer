# Trying to download things that don't exist:
import urllib.request
try:
    webpage = urllib.request.urlopen('http://wwww.google.com')
except:
    print('Could not Access webpage')
else:
    for line in webpage:
        print(line)
# Overloading a circuit breaker:
class circuitbreaker:
    def __init__(self, max_amps):
        self.capacity= max_amps # max capacity in amps. 
        self.load = 0 # present load in amps
    def connect(self, amps):
        self.load += amps
cb = circuitbreaker(30)
print(cb.load)

# Error Checking:
class circuitbreaker:
    def __init__(self, max_amps):
        self.capacity= max_amps # max capacity in amps. 
        self.load = 0 # present load in amps
    def connect(self, amps):
        if self.load + amps >self.capacity:
            raise Exception ('Connection will exceed capacity')
        elif self.load + amps < 0:
            raise Exception('Connection will cause a negative load')
        else:
            self.load += amps
       
cb = circuitbreaker(30)
print(cb.load)
cb.connect(12)
print(cb.load)
cb.connect(-1)
print(cb.load)

# Handling Household Problems:
class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
    def __srt__(self):
        return "The {} is {}!".format(self.device, self.problem)
class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)
def cause_error(error_type):
    if error_type == 'electrical':
        raise ElectricalError('circuit breaker', 'overloaded')
    elif error_type == 'plumbing':
        raise PlumbingError('dishwasher','spraying water')
    else:
        raise Exception('Generic household problems')
try:
    cause_error('electrical')
except ElectricalError as e:
    print(e)
    print('Fix it myself!')
except PlumbingError as e:
    print(e)
    print('Call the plumenger')
except: 
    print('Call the landlord')




