from math import log


def entropy(text) -> float:
    stat = {}
    file_size = 0
    result = 0

    for char in text:
        if char in stat:
            stat[char] += 1
        else:
            stat[char] = 1

    for char in stat:
        # print("{} <=> {}".format(char, stat[char]), file=sys.stderr)
        file_size += stat[char]

    for char in stat:
        p = stat[char] / file_size
        result -= p * log(p, 2)

    return result


files = [
    "demo24.bmp",
    "nicelandscape.bmp",
]

if __name__ == "__main__":
    for i in files:
        f = open(i, 'rb')
        H = entropy(f.read())
        print(f"Entropy of {i} -> {H:.4f}")
        f.close()
