from collections import Counter
from itertools import chain

black = ""
green = "?????"
known_excludes = ["", "", "", "", ""]
orange = "" + "".join(known_excludes)

matches = []
all_words = sorted(word for word in open("words.txt").read().splitlines())
for word in all_words:
    if (
        # non the the words letter are in the blacks
        all(l not in word for l in black)
        # all of the words letters are in the oranges
        and all(l in word for l in orange)
        # the word has the orange letters at not that that place
        and all(w not in e for e, w in zip(known_excludes, word))
        # all known letters are at the right place
        and all(g == "?" or g == w for g, w in zip(green, word))
    ):
        matches.append(word)

# get a list of letters ordered by how many times the appear in the matches
# letter at position 0 is the one which appears least time
c = list(reversed(Counter(chain.from_iterable(matches)).keys()))


def order(w):
    return sum(c.index(letter) for letter in set(w))


matches.sort(key=order, reverse=True)

print("First 10 Results:\n" + "\n".join(matches[:10]))
print()
print(f"Number of all results: {len(matches)}")
