message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊️️",
    ":(": "☹️"
}

out = ""
for word in words:
     out += emojis.get(word, word) + " "

print(out)