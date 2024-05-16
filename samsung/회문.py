T = int(input())

for tc in range(1, T + 1):

    words = input()

    boolean = 1

    for i in range(len(words)):
        if words[i] == words[-(i + 1)]:
            continue
        else:
            boolean = 0

    print("#" + str(tc) + " " + str(boolean))
