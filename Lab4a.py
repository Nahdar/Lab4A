

import HashTable
import time
import math


# Cosine similarity calculation
def cos_sim(table, key1, key2):
    node1 = table.search(key1)
    node2 = table.search(key2)

    dot_product = 0
    magnitude1 = 0
    magnitude2 = 0

    for i in range(len(node1.embedding)):
        dot_product = dot_product + (node1.embedding[i] * node2.embedding[i])

    for i in range(len(node1.embedding)):
        magnitude1 = magnitude1 + (node1.embedding[i] * node1.embedding[i])
        magnitude2 = magnitude2 + (node2.embedding[i] * node2.embedding[i])

    magnitude1 = math.sqrt(magnitude1)
    magnitude2 = math.sqrt(magnitude2)

    magnitude1 = magnitude1 * magnitude2

    return dot_product / magnitude1


# Opening file and initializing variables
file = "glove.6B.50d.txt"


# Filling Table
start = time.process_time()
table = HashTable.HashTable(400000)

with open(file) as dictionary:

    for line in dictionary:

        words = line.split()

        alphabetical = True

        #print("First word: " + words[0] + "--------------------------")

        #print("Length of the word: " + str(len(words[0])))

        for i in range(len(words[0]),):

            #print("i: " + str(i))
            #print("Letter checked: " + words[0][i])

            if 'a' >= words[0][i] >= 'z':
                alphabetical = False
                break

        if alphabetical is True:
            #print("Is alphabetical!!")
            for i in range(1, 51, 1):
                words[i] = float(words[i])
            table.insert(HashTable.HTNode(words.pop(0), words))

end = time.process_time()
print("Insertion(HashTable): " + str(end - start))


# Reading second file
start = time.process_time_ns()
with open("support.txt") as support:
    for line in support:
        print(line.split()[0] + " " + line.split()[1] + " " + str(cos_sim(table, line.split()[0], line.split()[1])))
end = time.process_time_ns()
print("Search: " + str(end - start))


# Make file with all words
depth_per_node = open("depth_per_node.txt", "w")
with open("all_words.txt", "w") as all_words:
    for i in range(table.size-1):
        count = 0
        head = table.table[i]
        while head is not None:
            all_words.write(head.key + "\n")
            count += 1
            head = head.next
        depth_per_node.write("Nodes in index " + str(i) + ": " + str(count) + "\n")
