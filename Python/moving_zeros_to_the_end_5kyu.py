def move_zeros(array):
    count = 0
    emptylist = []
    for iteration, i in enumerate(list(array)):
        print("each iteration:", iteration)
        if i == 0:
            array.remove(i)
            emptylist.append(i)
            # testing whether this removes 0s from the array and adds them in to emptylist
            print("array currently", array)
            print("emptylist currently: ", emptylist)
        else:
            count +=  1
            continue
    array += emptylist
    return array

#testing function with different number sets
callfunc = move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
callfunc2 = move_zeros([13, 0, 4, 1, 6, 1, 8, 3, 0, 100])
callfunc3 = move_zeros([78,1,38,47,22])
callfunc4 = move_zeros([0,2,8,0])
print(callfunc)