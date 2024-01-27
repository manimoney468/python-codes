def ss(a):
    for i in range(0, 7):
        for j in range(i + 1, 7): // to the left side manam place chestam  so that ekkuva best 
// 1 number emo 1, emo 2 thothi ,1 emo 3 thothi ,1 emo 4 thothi ,..... camp[are chesi 1 place lo least value untadi 
// next iteration lo   2 number emo 3, emo 2 thothi ,2 emo 4 thothi ,2 emo 5 thothi ,..... campare chesi 2nd  place lo second  least value untadi 
            if a[j] < a[i]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp

a = [2, 7, 3, 6,  5, 11, 9]
ss(a)

print(a)
