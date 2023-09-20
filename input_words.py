wordsarray = []
word = ""

def print_all_caps(array):
    for word in array:
        print(word.upper())

def print_all_lowercase(array):
    for word in array:
        print(word.lower())

def print_all_reversed(array):
    for word in array:
        print(word[::-1])

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
    choice = input(
"""
Enter: 
    1 for ALL CAPS, 
    2 for ALL LOWERCASE, 
    3 for ALL REVERSED
    OR 0 to exit: """)
    if choice == '1':
        print_all_caps(wordsarray)  
    elif choice == '2': 
        print_all_lowercase(wordsarray)
    elif choice == '3':
        print_all_reversed(wordsarray)
    print("======================================================================================================")





