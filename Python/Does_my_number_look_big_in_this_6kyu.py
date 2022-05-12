def narcissistic(test):
    
    """
    Summary:
    A Narcissistic Number is a positive number which is the sum of its own digits, 
    each raised to the power of the number of digits in a given base. 
    In this Kata, we will restrict ourselves to decimal (base 10).

    Needs refactoring, perhaps next time.

    Args:
        value (integer): number to be tested

    Returns:
        boolean: is number narcisstic true/false
    """
    valueconv = str(value)
    raisednum = len(valueconv)
    print("this is raised number", raisednum)
    mapping = map(int,valueconv)
    makelist = list(mapping)
    print(makelist)
    emptylist = []
    for x in makelist:
        calc_narc = x ** raisednum
        appendlist = emptylist.append(calc_narc)
        #print(sum(emptylist))
        sumitup = sum(emptylist)
    if sumitup == value:
        return True
    else:
        return False



