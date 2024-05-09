N = int(input())

for i in range(1, N + 1):
    if str(i) in "3" or "6" or "9":
        count = 0
        count += str(i).count("3")
        count += str(i).count("6")
        count += str(i).count("9")

        for i in range(count):
            print("-")

    print(i)
