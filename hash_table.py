from hash_v1 import hash_v1

hash_table = {}
hash_func = hash_v1
buckets = 5


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def init_hash_table(buckets):
    for index in range(buckets):
        hash_table[index] = None


def load_data_from_file():
    with open("30k.txt", "r") as f:
        for a_word in f:  # read a line, till the end of file. One word in each line
            a_word = a_word.strip()  # remove new line character
            hash_value = hash_func(a_word)  # generate the hash value
            index = hash_value % buckets  # calculate bucket index.
            add_data(index, a_word)


def add_data(index, data):
    if hash_table[index] is None:
        hash_table[index] = Node(data)
    else:
        current = hash_table[index]
        previous = None
        while current:
            previous = current
            current = current.next
        previous.next = Node(data)


def add_new_string(data):
    hash_value = hash_func(data)  # generate the hash value
    index = hash_value % buckets  # calculate bucket index.
    add_data(index, data)


# Returns true if a string exists in hash table. Otherwise false
def search(data):
    hash_value = hash_func(data)  # generate the hash value
    index = hash_value % buckets  # calculate bucket index.
    print(index)
    current = hash_table[index]
    while current:
        if current.data == data:
            return True
        current = current.next
    return False


if __name__ == "__main__":
    init_hash_table(buckets)
    load_data_from_file()
    add_new_string("try try try")
    print(hash_table)
    print(search("the"))  # returns true
    print(search("try try trry"))  # returns false
