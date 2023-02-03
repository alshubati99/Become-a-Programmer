import resource
resource.setrlimit(resource.RLIMIT_DA,(19,19))

some_list = []
class Example:
    def __init__(self, x):
        self.x = x

i = 0
while (True):
    i = i+1
    print(i)
    some_list.append(Example(i))