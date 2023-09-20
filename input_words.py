wordsarray = []
word = ""

while word.lower() != "exit":
    word = input("Please enter a word to add to the array or enter \"exit\":")
    if word.lower() != "exit": wordsarray.append(word)

print("======================================================================================================")
print("\t Words array")
for word in wordsarray:
    print(word)

print("======================================================================================================")
