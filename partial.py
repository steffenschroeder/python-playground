from functools import partial

def say(first, last):
    print(" ".join((first,last)))

say2 = lambda x, y: print(" ".join((x, y)))

say("hello", "world")
say2("hello", "world")
say_hello = partial(say, "hello")

say_hello('steffen')






