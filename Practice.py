list = [1,2,3,4,5,6,7,8,9,10]
print (list)

def reverse(list):
    return list[::-1]

print (reverse(list))

def three_seven(list):
    for num in list:
        if num == 3 or num == 7:
            continue
        print(num, end = " ")

three_seven(list)

print (" ")
myset = set(list)
print(myset)
print(type(myset))

myset.remove(8)
print(myset)

print(sorted(myset))