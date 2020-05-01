customer = {"name": "John Smith", "age": 30, "is_verified": True, "hest": "Ku"}

print(customer.get("hest"))

# Task
phone = input("Phone: ")

numWords = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine ",
    "0": "Zero"
}

wordList = ""
for digit in phone:
    wordList += numWords.get(digit)
print(wordList)