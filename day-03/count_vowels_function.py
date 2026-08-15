def count_vowels(string):
    vowels = ['A','E','I','O','U','a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count
string = "Hello World"
print(count_vowels(string))


