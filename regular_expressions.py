import re
hand = open("newdata.txt")
lst = list()
for line in hand:
    number = re.findall('[0-9]+',line)
    lst = lst + number
sum = 0
for num in lst:
    sum = sum + int(num)
print(sum)
