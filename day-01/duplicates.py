objects = ["a", "b", "c", "d", "e", "f", "b", "e", "i", "a"]
duplicates = []
for i in objects:
    if objects.count(i) > 1 and i not in duplicates:
        i = duplicates.append(i)
print("duplicate elements:", duplicates)
