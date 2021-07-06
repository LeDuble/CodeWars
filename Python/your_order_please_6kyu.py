# Your task is to sort a given string. 
# Each word in the string will contain a single number. 
# This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. 
# So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.

def order(sentence):
    #1) splits the sentence in to a list
    x = sentence.split()
    #2) sorts the list using order_numbers function in ascending order
    s = sorted(x, key=order_numbers)
    return " ".join(s)

def order_numbers(number):
    for i in number:
        if i.isdigit():
            return int(i)

print(order("is2 Thi1s T4est 3a"))