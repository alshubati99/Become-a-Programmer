# Rolodex full of friends: 
# Dictionary of names/numbers pairs:
rolodex = {
    'kh': 3375857,
    'gh': 4978647,
    'ch': 2554646,
    'sh': 9475837,
}
print(rolodex)
print(rolodex['kh'])
rolodex['m']= 235546
print(rolodex)
rolodex['kh']= (2423535, 3375857)
print(rolodex)

def caller_id(lookup_number):
    for name, num in rolodex.items():
        if num == lookup_number:
            return name
        
print(caller_id(235546))

