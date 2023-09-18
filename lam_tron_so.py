t = int(input())

for _ in range(t):

    a = list(map(int, str(input())))

    a.reverse()

    for i in range(len(a)-1):
        if(int(a[i]) >= 5):
            a[i] = 0
            if(i + 1 >= len(a)):
                a.append(1)
            else:
                a[i + 1] += 1
        else :
            a[i] = 0
    
    a.reverse()

    print(''.join(map(str, a)))

    

