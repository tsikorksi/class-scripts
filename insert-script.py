"""
Input list1, list2
List3 = []
Check = true
For i <- 0 to length(list2)
    IF check == True
            For j <- 0 to length(list1)
                IF list1[j] > list2[i] THEN
                    List1.insert(j – 1, list2[i])
                    Check = false
    Check = true
Print(list1)
Print(list2)
Print(list3)


"""
list1 = [2, 5, 15, 36, 47, 56, 59, 78, 156, 244, 268]
list2 = [18, 39, 42, 43, 66, 69, 100]
list3 = []
list3 += list1
added = True

for i in range(0, len(list2)):
    for j in range(0, len(list1)):
        if list1[j] > list2[i]:
            if added:
                list3.insert(j, list2[i])
                added = False
    added = True

print(list1)
print(list2)
print(list3)
