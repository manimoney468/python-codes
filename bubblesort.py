def bubblesort(a, l):
    for i in range(l - 1):
        for j in range(0, l - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

    return a

a = [2, 7, 3, 6, 5, 11, 9]
y = bubblesort(a, 7)
print(y)
