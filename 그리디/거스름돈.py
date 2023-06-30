n = 1260
count = 0
#11
money = [500,100,50,10]

for i in money:
    count += n // money
    n = n % money

print(count)



