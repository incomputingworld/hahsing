from random import randint, choices
import string
from hash_v1 import hash_v1


# Function counts number of words each bucket will contain.
def data_distribution_in_buckets(bucket_size=5, hash_func=hash_v1):
    indexes = [(x, 0) for x in range(0, bucket_size)]
    hash_table = dict(indexes)

    # words are stored in a file.
    with open("30k.txt", "r") as f:
        for line in f:  # read a line, till the end of file. One word in each line
            a_word = line.strip()  # remove newline character
            hash_value = hash_func(a_word)  # generate the hash value
            index = hash_value % bucket_size  # calculate bucket index.
            hash_table[index] += 1  # Update count

    # show the distribution of data
    total_count = sum(hash_table.values())
    print(total_count)
    for key, value in hash_table.items():
        print(f"Bucket - {key + 1} - Values - {value} - "
              f"%age - {round(((value / total_count) * 100), 2)}")


def generate_random_string(str_min_length=3, str_max_length=15):
    string_length = randint(str_min_length, str_max_length)
    random_string = ''.join(choices(string.ascii_letters, k=string_length))
    return random_string


# Function counts number of random words each bucket will contain.
def data_distribution_with_random_data(bucket_size=5, hash_func=hash_v1):
    indexes = [(x, 0) for x in range(0, bucket_size)]  # creates a list of tuples

    # create a dictionary from tuples. Each key represents a bucket. Value represents the count
    hash_table = dict(indexes)

    for i in range(5 * 1024 * 1024):
        random_string = generate_random_string(str_min_length=5, str_max_length=30)
        hash_value = hash_func(random_string)
        index = hash_value % bucket_size
        hash_table[index] += 1

    total_count = sum(hash_table.values())
    print(total_count)
    for key, value in hash_table.items():
        print(f"Bucket - {key + 1} - Values - {value} - "
              f"%age - {round(((value / total_count) * 100), 2)}")


"""
Additional test function not mentioned in the article. This function generates
hash value of randomly generated IDs of 9-digits. Prefix and suffix is optional.
This implementation creates an imbalance where Bucket#2 gets > 24% of the values.
"""


def generate_random_id(prefix='P', suffix=None, padding=True):
    random_id = ''
    if prefix:
        random_id = prefix

    number = randint(1, 999999999)
    if padding:
        random_id += f"{number:09d}"
    else:
        random_id += str(number)

    if suffix:
        random_id += suffix

    return random_id


def data_distribution_with_random_ids(bucket_size=5, hash_func=hash_v1):
    indexes = [(x, 0) for x in range(0, bucket_size)]  # creates a list of tuples

    # create a dictionary from tuples. Each key represents a bucket. Value represents the count
    hash_table = dict(indexes)

    for i in range(5 * 1024 * 1024):
        random_string = generate_random_id()
        hash_value = hash_func(random_string)
        index = hash_value % bucket_size
        hash_table[index] += 1

    total_count = sum(hash_table.values())
    print(total_count)
    for key, value in hash_table.items():
        print(f"Bucket - {key + 1} - Values - {value} - "
              f"%age - {round(((value / total_count) * 100), 2)}")


if __name__ == "__main__":
    # data_distribution_in_buckets()
    data_distribution_with_random_data()
    # data_distribution_with_random_ids()
