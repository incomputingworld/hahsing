
def hash_v1(data):
    hash_value = 0

    data = data.encode("utf-8")

    for c in data:
        hash_value = hash_value ^ c  # XoR each byte with previous bytes

    return hash_value


