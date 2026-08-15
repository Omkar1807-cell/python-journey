def remove_duplicates(list):
    duplicates = []
    for i in list:
        if i not in duplicates:
            duplicates.append(i)
    return duplicates
list = [1,1,2,2,2,3,4,5,5,6]
print(remove_duplicates(list))

