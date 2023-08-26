from lettershape import LetterShape

letterbox = LetterShape("ico", "gns", "apl", "mre")

print("Importing words...")
words_file = open("words.txt", "r")
words_list = words_file.read().lower().split("\n")
words_file.close()

print(f"Filtering {len(words_list)} words...")
words_list = list(filter(lambda word: letterbox.is_valid(word), words_list))

print(f"Creating pairs for {len(words_list)} words...")
words_pairs = []
for word_1 in words_list:
    for word_2 in words_list:
        words_pairs.append((word_1, word_2))
            
print("Searching for valid pairs...")
words_pairs = list(filter(lambda pair: (letterbox.is_valid(pair[0], pair[1])) and (letterbox.get_remainder(pair[0] + pair[1]) == ""), words_pairs))
print(f"FOUND {len(words_pairs)} VALID PAIRS.")

print("Writing valid pairs to file...")
formatted_words_pairs = []
for pair in words_pairs:
    # if len(pair[0] + pair[1]) == 13:
    formatted_words_pairs.append(pair[0] + " + " + pair[1])
formatted_words_pairs.sort()
formatted_words_pairs.sort(key=len)
results_file = open("results.txt", "w")
results_file.write("\n".join(formatted_words_pairs))
results_file.close()

print("Finished.    ")