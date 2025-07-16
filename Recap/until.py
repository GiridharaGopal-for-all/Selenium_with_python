q = "hi giri "
w = q.split(" ")
e = {}
for i in w:
    if i in e:
        e[i] += 1
    else:
        e[i] = 1
max_word = None
max_count = 0
for word, count in e.items():
    if count % 2 == 0 and count > max_count:
        max_count = count
        max_word = word
if max_word:
    print(f"{max_word}:{max_count}")
else:
    print("No word found with maximum even count.")
