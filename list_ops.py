def map_clone(op, list):
    return [op(i) for i in list]


def length(l):
    for i, _ in enumerate(l): pass
    return i + 1 if l else 0


def filter_clone(op, l):
    return [i for i in l if op(i)]


def reverse(l):
    return l[::-1]


def append(l, args):
    return l + [args]


def foldl(op, l, initial):
    result = initial
    for item in l:
        result = op(result, item)
    return result


def foldr(op, l, initial):
    result = initial
    for item in reverse(l):
        result = op(item, result)
    return result


def flat(l):
    result = []
    for item in l:
        if isinstance(item, list):
            result += flat(item)
        else:
            result.append(item)
    return result


def concat(first, second):
    result = []
    all_or_nothing = lambda l: l if l else []
    result += all_or_nothing(first)
    result += all_or_nothing(second)

    return result
