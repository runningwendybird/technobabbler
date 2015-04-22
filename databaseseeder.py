
import sys
import random


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # a list of all the words that appear in the text
    markov_list = []
    #
    markov_keys = []
    #
    markov_dict = {}

    # Goes line by line through the source text. Strips each line. 
    # splits the words on the spaces. Goes through each word, appending to 
    # Markov list. The order of the words is retained.

    for l in corpus:
        line = l.strip()
        words = line.split(" ")
        for word in words:
            word = word.lower()
            markov_list.append(word)

    
    # Goes through the Marov list and creates a dictionary with each work
    for i in range(0, len(markov_list)-2):
        if (markov_list[i], markov_list[i+1]) in markov_dict:
            markov_dict[(markov_list[i], markov_list[i+1])].append(markov_list[i+2])
        else:
            markov_dict[(markov_list[i], markov_list[i+1])] = [markov_list[i + 2]]

    for keys in markov_dict.keys():
        if '\r' in keys[0] or '\r' in keys[1]:
            del markov_dict[keys]

    return markov_dict



def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    current_key = random.choice(chains.keys())
    s = current_key[0] + " " + current_key[1]
    count = 0
    while current_key in chains and count < 150:
        #print current_key
        next_word = random.choice(chains[current_key])
        #print next_word
        s = s + " " + next_word
        current_key = (current_key[-1], next_word)
        count = count + 1
    return s


def main():
    args = sys.argv

    script, file_to_open = args

    input_file = open(file_to_open)
    chain_dict = make_chains(input_file)
    random_text = make_text(chain_dict)
    print random_text
    input_file.close()


if __name__ == "__main__":
    main()