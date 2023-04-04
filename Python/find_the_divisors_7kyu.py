def divisors(integer):
    empty_list = []
    if integer > 1:
        all_together = [integer % i for i in range(2,integer)]
        if 0 in all_together:
            for idx, i in enumerate(all_together):
                if i == 0:
                    empty_list.append(idx+2)
            return empty_list      
        else:
            return f"{integer} is prime"

print(divisors(15) == [3,5])
print(divisors(253) == [11,23])
print(divisors(24) == [2,3,4,6,8,12])
print(divisors(25) == [5])
print(divisors(13) == "13 is prime")
print(divisors(3) == "3 is prime")
print(divisors(29) == "29 is prime")
