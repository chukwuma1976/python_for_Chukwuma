wordsarray = []
word = ""

def print_all_caps(array):
    for word in array:
        print(word.upper())

def print_all_lowercase(array):
    for word in array:
        print(word.lower())

while word.lower() != "exit":
    word = input("Please enter a word to add to the array or enter \"exit\": ")
    if word.lower() != "exit": wordsarray.append(word)

print("======================================================================================================")
print("\t Words array")
for word in wordsarray:
    print(word)

print("======================================================================================================")

choice = None
while choice != '0' :
    choice = input("Enter the number 1 for ALL CAPS, number 2 for ALL LOWERCASE, or number 0 to exit: ")
    if choice == '1':
        print_all_caps(wordsarray)  
    elif choice =='2': 
        print_all_lowercase(wordsarray)
    print("======================================================================================================")





