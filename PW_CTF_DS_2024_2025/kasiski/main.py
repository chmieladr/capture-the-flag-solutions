import string

ALPHABET = string.ascii_lowercase + string.digits  # custom alphabet used


def get_offset(a: chr, b: chr) -> int:
    return abs(ALPHABET.find(a) - ALPHABET.find(b))


# Example of custom offsets for each position (uncomment and modify if needed)
# Fill based on a singular example of decrypted character!
# The proper format of each entry (aka line) is: <position>: determine_offset(<currently_obtained_char>, <correct_char>)
OFFSET_TWEAK_DICT = {
    # 11: get_offset('9', 'o'),
    # 22: get_offset('9', 'o'),
    # 42: get_offset('6', 'l'),
}


def process_text(input_path: str = "container/index.txt", offset_tweak_dict: dict | None = None) -> str:
    if offset_tweak_dict is None:
        offset_tweak_dict = {}
    with open(input_path) as file:  # reading the input encrypted text
        text = file.read()

    offsets = {}  # for storing offsets at each pos
    new_text = ""  # for storing the decrypted text

    for i in range(60):
        pos = i
        freq = {}
        while pos < len(text):
            if text[pos] in freq:
                freq[text[pos]] += 1
            else:
                freq[text[pos]] = 1
            pos += 60
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        offsets[i] = ALPHABET.find(freq[0][0]) - 4  # "- 4" as 'e' letter offset - the most common letter in English

    for tweak_pos, tweak_offset in offset_tweak_dict.items():
        offsets[tweak_pos] += tweak_offset

    print(offsets)

    for i, char in enumerate(text):  # modifying each character based on earlier determined offset
        new_text += ALPHABET[(len(ALPHABET) + ALPHABET.find(char) - offsets[i % 60]) % len(ALPHABET)]

    return new_text


if __name__ == "__main__":
    with open("text.txt", "w") as f:  # saving the result
        f.write(process_text(offset_tweak_dict=OFFSET_TWEAK_DICT))
