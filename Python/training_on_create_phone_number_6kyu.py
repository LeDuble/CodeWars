import random as rnd
def create_phone_number(n):
    """Create a phone number format out of random set of numbers within a list.

    Args:
        n {integer}: a set of numbers 
    """
    loop = [str(i) for i in n]
    
    #turns items in a tuple into a string
    conc = "".join(loop)
    
    start_numbers = conc[0:3]
    mid_numbers = conc[3:6]
    last_numbers = conc[6:10]

    return("(" + start_numbers + ")" + " " + mid_numbers + "-" + last_numbers)
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
rng_numbers = rnd.shuffle(list_of_numbers)
print(create_phone_number(list_of_numbers))