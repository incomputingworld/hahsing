from random import randint, choices
import string
import time

from hash_v1 import hash_v1


def test_one_way():
    alphabets = [chr(x) for x in range(65, 75)]
    numbers = [x for x in range(0, 10)]

    for number in numbers:
        print(f"{number} - {hash_v1(str(number))}", end=", ")
    print()  # prints a blank line
    for alphabet in alphabets:
        print(f"{alphabet} - {hash_v1(str(alphabet))}", end=", ")


def test_avalanche_effect():
    var1 = "tim"
    var2 = "tin"

    print(f"{var1} - {hash_v1(var1)}")
    print(f"{var2} - {hash_v1(var2)}")


# Generates a random string 3 to 15 characters long
def generate_random_string(str_min_length=3, str_max_length=15):
    string_length = randint(str_min_length, str_max_length)
    random_string = ''.join(choices(string.ascii_letters, k=string_length))
    return random_string


def test_collision(str_min_length=3, str_max_length=15, hash_func=hash_v1):
    all_hashes_and_data = {}  # stores all the data and corresponding hash values

    for i in range(1500):
        random_string = generate_random_string(str_min_length, str_max_length)
        hash_value = hash_func(random_string)

        if hash_value in all_hashes_and_data:
            if random_string != all_hashes_and_data[hash_value]:
                print(f"!!!Collision Detected!!! - at position {len(all_hashes_and_data)}")
                print(f"{hash_value} - {random_string}")
                print(f"{hash_value} - {all_hashes_and_data[hash_value]}")
                break

        all_hashes_and_data[hash_value] = random_string


def test_speed(str_min_length=3, str_max_length=15, hash_func=hash_v1):
    for i in range((15 * 1024 * 1024)):
        random_string = generate_random_string(str_min_length, str_max_length)
        hash_func(random_string)


def test_speed_big_string(string_size=1024, hash_func=hash_v1):
    i = 0
    hash_value = 0
    char = ''
    while i < string_size:
        char = ''.join(choices(string.ascii_letters, k=1))
        hash_value = hash_value ^ hash_func(char)
        i += 1
    print(hash_value)


if __name__ == "__main__":
    # test_one_way()
    # test_avalanche_effect()
    # test_collision()
    # start_time = time.time()
    # test_speed()
    # test_speed_big_string(32 * 1024 * 1024)
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"Function execution time: {execution_time:.6f} seconds")
