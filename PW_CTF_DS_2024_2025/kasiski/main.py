import string

ALPHABET = string.ascii_lowercase + string.digits  # custom alphabet used

if __name__ == "__main__":
    f1 = open("container/index.txt", "r")  # reading the input encrypted text
    text = f1.read()
    f1.close()

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

    print(offsets)

    for i, char in enumerate(text):  # modifying each character based on earlier determined offset
        new_text += ALPHABET[(len(ALPHABET) + ALPHABET.find(char) - offsets[i % 60]) % len(ALPHABET)]

    f2 = open("text.txt", "w")  # saving the result
    f2.write(new_text)
    f2.close()
