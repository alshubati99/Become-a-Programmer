# Lists' methods:
row = ['ford', 'Audi', 'BMW', 'lexus']
row.append('Mercedes')
print(row)
print(row[4])
row[2]= 'jeep'
print(row)
row.insert(0, 'kia')
print(row)
print(row.index('Mercedes'))
row.pop(5)
print(row)
row.remove('lexus')
print(row)

# 2D list of lists:
list_2D = [['Toyota',  'Audi', 'BMW'], # 0th row
           ['lexus','jeep'],           # 1st row
           ['Hona','kia', 'Mazda']]    # 2nd row

# 3D list of lists of lists: 
list_3D = [
    [['Tesla','Fiat','BMW'],['Honda','jeep'],['Saab','kia','ford']],   # 0th row 
    [['subaru','Nissan'],['Volvo']],                                   # 1st row
    [['mazda','chevy'],['volkswage']]                                  # 2nd row
]
print(list_2D)
print(list_3D)
print(list_2D[2][1])
print(list_3D[0][2][1])
for car in list_3D:
    print(car)

# To print the cars individually: 
for floor in list_3D:
    for row in floor:
        for car in row:
            print(car)
# Tuples:
my_tuple = ('a','b','c',1,2,3)
print(my_tuple[2])
print(my_tuple)
 
# Where is My Mouse?
import tkinter
def mouse_click(event):
    # retrieve XY coords as a tuple:
    coords = root.winfo_pointerxy()
    print('coords: {}'.format(coords))
    print('X: {}'.format(coords[0]))
    print('Y: {}'.format(coords[1]))
root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()