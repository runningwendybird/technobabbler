
import sys
import random
import model


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



# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""

#     #selects a random key
#     current_key = random.choice(chains.keys())
#     # creates a string with the first two words.
#     s = current_key[0] + " " + current_key[1]
#     count = 0
#     while current_key in chains:
#         #print current_key
#         next_word = random.choice(chains[current_key])
#         #print next_word
#         s = s + " " + next_word
#         current_key = (current_key[-1], next_word)
#         count = count + 1
#     return s

def add_author_topic_and_paper():
    """Checks to see if author is in db and adds him/her if not.
    Adds paper to database."""
    #get's author's name from the user.
    
    author_first = input("Enter author's first name: ")
    author_last = input("Enter author's last name: ")
    
    #checks to see if author is in the db. 
    # If not, adds the author to the database and
    # gets creates an author object. 

    author = model.find_author_by_name(author_first, author_last)

    if author == None:

        # creates new author object and adds it to the database.

        new_author_obj = model.Author(first = author_first.lower(), last = author_last.lower())
        model.sqla_session.add(new_author_obj)
        model.sqla_session.commit()

        #gets the author object back out of the database.
        author = model.find_author_by_name(author_first, author_last)

    else:

        pass

    # Checks to see if topic is in db and adds it if not.

    topics = model.find_all_topics()
    print "Here are all the topics currently in the database:"

    for i in range(len(topics)):
        print i, topics[i]

    avaiable = input("enter y if the topic of this paper is displayed. enter another key if not." )

    if available.lower() == "y":
        select = int(input("please input the number that appears next to the topic of the source text. "))
        







def main():
    args = sys.argv

    script, file_to_open = args

    input_file = open(file_to_open)
    chain_dict = make_chains(input_file)
    # random_text = make_text(chain_dict)
    # print random_text
    input_file.close()


if __name__ == "__main__":
    main()