# Loading a dishwasher:
sink = ['bowl','plate','cup']
for dish in sink:
    print('put {} in the dishwasher'.format(dish))

for dish in list(sink):
    print('put {} in the dishwasher'.format(dish))
    sink.remove(dish)
print(sink)

# Scrubbing a stuborn pan:
import random
dirty = True # state of the pan
scrub_count = 0 # number of scrubs
while(dirty):
    scrub_count +=1
    print('scrub the pan : {}'.format(scrub_count))
    print('Rinse and chek if the pan is clean')
    if not random.randint(0,9):
        print('All clean!')
        dirty = False
    else:
        print('Still dirty...')

# you can use break in for loop!