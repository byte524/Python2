from random import randint

ls1 = []

for i in range(20):
    ls1.append(randint(1,200))
print(ls1) #чтобы посмотреть изначальный вариант списка


def test_sort(N):
    cycle = True
    while cycle:
        cycle = False
        for i in range(len(N) - 1):
            if N[i] > N[i + 1]:
               
                N[i], N[i + 1] = N[i + 1], N[i]
                
                cycle = True

test_sort(ls1)
print(ls1)
