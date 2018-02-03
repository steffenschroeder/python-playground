import bisect
import operator


# a = [1, 3, 3, 3, 5, 7]
# print(bisect.bisect_left(a, 3))


class KeyifyList(object):
    def __init__(self, inner, key=lambda x: x):
        self.inner = inner
        self.key = key

    def __len__(self):
        return len(self.inner)

    def __getitem__(self, k):
        return self.key(self.inner[k])

d = {1: 2, 3: 4, 4: 4, 5: 6, 7: 8}


def get_build(version):
    print("Called: %s" % version)
    return d.get(version, 0)


if __name__ == '__main__':
    L = [(0, 0), (1, 5), (2, 10), (3, 15), (4, 20)]
    #assert bisect.bisect_left(KeyifyList(L, lambda x: x[0]), 3) == 3
    #assert bisect.bisect_left(KeyifyList(L, lambda x: x[1]), 3) == 1

    m = list(d.keys())
    #assert bisect.bisect_left(KeyifyList(m, get_build), 4) == 1
    assert bisect.bisect_left(KeyifyList(m, get_build), 9) == len(m)