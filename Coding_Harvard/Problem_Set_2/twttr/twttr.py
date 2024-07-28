answer = input("Input: ")
print (end="")
for letter in answer:
    if not letter in ["a", "e","i" ,"u" ,"o","O"]:
        print(letter , end="")
print()