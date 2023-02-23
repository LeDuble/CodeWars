def descending_order(num):
    """Rearrange the given numbers in descending order.

    Args:
        int : takes integer as arg.

    Returns:
       int : returns given number in descending order as integer.
    """
    temp_num = [i for i in str(num)]
    return int("".join(sorted(temp_num, reverse=True)))
    
descending_order(123456)