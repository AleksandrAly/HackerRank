def New_Sorting(newstd):
    for i in range(0, t):
        newstd = input()
        a = [x for k, x in enumerate(newstd) if not k % 2]
        b = [x for k, x in enumerate(newstd) if k % 2]
        print(''.join(a), ''.join(b))
    return

t = int(input().strip())
newstd = []
#print('\n'.join(newstd))
stdout = New_Sorting(newstd)

