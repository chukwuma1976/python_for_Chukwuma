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

def print_on_one_line(array):
    line = ""
    for word in array:
        line = line + word + " "
    print(line)

def write_as_a_sentence(array):
    line = ""
    for word in array:
        line = line + word + " "
    print(line + ".")
    

while word.lower() != "exit":
    word = input("Please enter a word to add to the array or enter \"exit\": ")
    if word.lower() != "exit": wordsarray.append(word)

print("======================================================================================================")
print("\t Words array")

print(wordsarray)

print("======================================================================================================")


choice = None
while choice != '0' :
    choice = input(
"""
Enter: 
    1 for ALL CAPS, 
    2 for ALL LOWERCASE, 
    3 for ALL REVERSED,
    4 to PRINT ON ONE LINE,
    5 to WRITE AS A SENTENCE
    OR 0 to exit: """)
    if choice == '1':
        print_all_caps(wordsarray)  
    elif choice == '2': 
        print_all_lowercase(wordsarray)
    elif choice == '3':
        print_all_reversed(wordsarray)
    elif choice == '4':
        print_on_one_line(wordsarray)
    elif choice == '5':
        write_as_a_sentence(wordsarray)
    print("======================================================================================================")





