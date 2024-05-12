from hashlib import algorithms_available, sha256


def list_supported_hash_functions():
    all_algorithms = sorted(algorithms_available)

    print("Available Hash Functions:")
    for algorithm in all_algorithms:
        print(algorithm)


def use_sha256(data):
    data = data.encode("utf-8")  # convert input to byte stream
    hash_obj = sha256(data)  # hash function returns a hash object.
    hash_value = hash_obj.digest()  # digest() hash value in byte format
    hash_hex_value = hash_obj.hexdigest()  # hexdigest() hash value in hexadecimal format
    return hash_value, hash_hex_value


# if __name__ == "__main__":
#     print(use_sha256(""))
#     list_supported_hash_functions()