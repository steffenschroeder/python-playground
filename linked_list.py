import unittest


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None
        self._length = 0

    def push(self, value):
        self._length += 1
        if self.last is None:
            self.first = self.last = Item(value)
        else:
            item_to_add = Item(value, prev_item=self.last)
            self.last.next_item = item_to_add
            self.last = item_to_add

    def pop(self):
        self._length -= 1
        value = self.last.value
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.last = self.last.prev_item
            self.last.next_item = None

        return value

    def unshift(self, value):
        self._length += 1
        if self.first is None:
            self.first = self.last = Item(value)
        else:
            item_to_add = Item(value, next_item=self.first)
            self.first.prev_item = item_to_add
            self.first = item_to_add

    def shift(self):
        self._length -= 1
        value = self.first.value
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next_item
            self.first.prev_item = None

        return value

    def __len__(self):
        return self._length

    def __iter__(self):
        other = LinkedList()
        other.current = self.first
        return other

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        val = self.current.value
        self.current = self.current.next_item
        return val

    def __repr__(self):
        return "[" + ", ".join(str(i) for i in self) + "]"


class Item:
    def __init__(self, value, next_item=None, prev_item=None):
        self.value = value
        self.next_item = next_item
        self.prev_item = prev_item


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_push_pop(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.pop(), 20)
        self.assertEqual(self.list.pop(), 10)

    def test_push_shift(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.shift(), 10)
        self.assertEqual(self.list.shift(), 20)

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(self.list.shift(), 20)
        self.assertEqual(self.list.shift(), 10)

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(self.list.pop(), 10)
        self.assertEqual(self.list.pop(), 20)

    def test_all(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.pop(), 20)
        self.list.push(30)
        self.assertEqual(self.list.shift(), 10)
        self.list.unshift(40)
        self.list.push(50)
        self.assertEqual(self.list.shift(), 40)
        self.assertEqual(self.list.pop(), 50)
        self.assertEqual(self.list.shift(), 30)

    def test_length(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(len(self.list), 2)
        self.list.shift()
        self.assertEqual(len(self.list), 1)
        self.list.pop()
        self.assertEqual(len(self.list), 0)

    def test_iterator(self):
        self.list.push(10)
        self.list.push(20)
        iterator = iter(self.list)
        self.assertEqual(next(iterator), 10)
        self.assertEqual(next(iterator), 20)


if __name__ == '__main__':
    unittest.main()
