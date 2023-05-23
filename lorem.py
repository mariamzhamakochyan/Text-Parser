with open("resources/lorem.txt", "r") as file:
    words = file.read().split()
    clean_words = [i.lower() for i in words if i.isalnum()]

with open("resources/words_alpha.txt", "r") as dict_file:
    dictionary = set(dict_file.read().split())

normalized_words = []
not_found = []
for word in clean_words:
    if word in dictionary:
        normalized_words.append(word)
    else:
        not_found.append(word)


print(normalized_words)
print(not_found)