

class HTNode:
    def __init__(self, key, embedding=None, next=None):
        self.key = key
        self.embedding = embedding
        self.next = next


class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def to_base26(self, num):
            return

    def to_decimal_from26(self, alpha):

        decimal = 0
        placement = 1

        for i in range(len(alpha) - 1, -1, -1):
            if alpha[i] is 'a':
                decimal += 0
            elif alpha[i] == 'b':
                decimal += 1 * placement
            elif alpha[i] == 'c':
                decimal += 2 * placement
            elif alpha[i] == 'd':
                decimal += 3 * placement
            elif alpha[i] == 'e':
                decimal += 4 * placement
            elif alpha[i] == 'f':
                decimal += 5 * placement
            elif alpha[i] == 'g':
                decimal += 6 * placement
            elif alpha[i] == 'h':
                decimal += 7 * placement
            elif alpha[i] == 'i':
                decimal += 8 * placement
            elif alpha[i] == 'j':
                decimal += 9 * placement
            elif alpha[i] == 'k':
                decimal += 10 * placement
            elif alpha[i] == 'l':
                decimal += 11 * placement
            elif alpha[i] == 'm':
                decimal += 12 * placement
            elif alpha[i] == 'n':
                decimal += 13 * placement
            elif alpha[i] == 'o':
                decimal += 14 * placement
            elif alpha[i] == 'p':
                decimal += 15 * placement
            elif alpha[i] == 'q':
                decimal += 16 * placement
            elif alpha[i] == 'r':
                decimal += 17 * placement
            elif alpha[i] == 's':
                decimal += 18 * placement
            elif alpha[i] == 't':
                decimal += 19 * placement
            elif alpha[i] == 'u':
                decimal += 20 * placement
            elif alpha[i] == 'v':
                decimal += 21 * placement
            elif alpha[i] == 'w':
                decimal += 22 * placement
            elif alpha[i] == 'x':
                decimal += 23 * placement
            elif alpha[i] == 'y':
                decimal += 24 * placement
            elif alpha[i] == 'z':
                decimal += 25 * placement
            placement *= 26

        return decimal


    def hash(self, key):
        return self.to_decimal_from26(key) % len(self.table)

    def insert(self, node):

        head = self.table[self.hash(node.key)]

        if head is None:
            self.table[self.hash(node.key)] = node
            return

        while head.next is not None:
            head = head.next

        head.next = node
        return

    def insert_key(self, key):

        node = HTNode(key, None)

        self.insert(node)

    def search(self, key):

        head = self.table[self.hash(key)]

        while head is not None and head.key != key:
            head = head.next

        return head
