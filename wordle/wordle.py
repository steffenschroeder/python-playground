black = ""
known = "?????"
known_excludes = ["", "", "", "", ""]
orange = "" + "".join(known_excludes)

matches = []
for word in sorted(word for word in open("words.txt").read().splitlines()):
    if (
        all(l not in word for l in black)
        and all(l in word for l in orange)
        and all(w not in e for e, w in zip(known_excludes, word))
        and all(k == "?" or k == w for k, w in zip(known, word))
    ):
        matches.append(word)

print("\n".join(matches))
print()
print(len(matches))
