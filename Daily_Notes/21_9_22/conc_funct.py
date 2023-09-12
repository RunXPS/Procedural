from sys import argv
def sanitize_word(w):
    out = ""
    for letter in w:
        if letter.isalnum() or letter == "'":
            out += letter
    return out

def read_words(filename):
    out = {}
    with open(filename, "r") as fp:
        for line in fp:
            line = line.lower()
            words = line.split()
            for w in words:
                w = sanitize_word(w)
                if w in out:
                    out[w] +=1
                else:
                    out[w] = 1
    return out

def write_dict(dictionary, filename):
    sorted_keys = sorted(dictionary.keys())
    with open(filename, "w") as fp:
        for word in sorted_keys:
            fp.write(f"{word}\t\t\t{dictionary[word]}\n")

def main ():
    input_file = argv[1]
    output_file = argv[1] + ".conc"
    all_of_text = read_words(input_file)
    write_dict(all_of_text, output_file)
main()