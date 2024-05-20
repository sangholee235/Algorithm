T = int(input())

for i in range(1,T+1):
    L,U,X = map(int,input().split())

    if X < L:
        print("#"+str(i)+" "+str(L-X))
    elif X > U:
        print("#"+str(i)+" -1")
    else:
        print("#"+str(i)+" 0")