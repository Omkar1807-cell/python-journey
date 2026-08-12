names =["Omkar" , "Aman" , "Shubham" , "Ice"]
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
count = 0
for name in names:
   for character in name:
       if character in vowels:
           count = count + 1
print("no of vowels:", count)
