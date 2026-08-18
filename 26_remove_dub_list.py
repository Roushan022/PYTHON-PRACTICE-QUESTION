def Duplicate(values):
    i = 0

    while i < len(values):
        j = i + 1

        while j < len(values):
            if values[i] == values[j]:
                print(values[i])
            j += 1

        i += 1
List_a=[2,3,4,2,5,6,3,4,9]
Duplicate(List_a)
