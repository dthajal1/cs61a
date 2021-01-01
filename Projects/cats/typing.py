"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    i = -1          # i is a counter
    for each_para in paragraphs :
        if select(each_para) == True :
            i += 1
        if i == k :
            return each_para
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def check_tru (word) :
        new_string = split(remove_punctuation(lower(word)))
        for goal in topic :
            for input in new_string :
                if input == goal:
                    return True
        return False
    return check_tru


# END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    correct, j, x =  0, 0, 0  #j, x are counters
    total = len(typed_words)
    if typed_words == []:
        return 0.0
    for x in range(min(len(typed_words), len(reference_words))) :
        each = typed_words[j]
        other = reference_words[j]
        j += 1
        if each == other :
            correct = correct + 1
    return (correct / total) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    char = len(typed)
    words = char / 5
    return words * (60 / elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    wrd_lstkey = {diff_function(user_word, x, limit) + (valid_words.index(x) + 1) * 0.00000001: x for x in valid_words}

    for x in valid_words:    # x is each word from valid_words
        if user_word == x:
            return x
    smallest = min(wrd_lstkey)
    if smallest < (limit + (1 * 0.000001)) :
        return wrd_lstkey[smallest]
    else:
        return user_word
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def find_diff (n_ch, diff ):
        if start [n_ch] != goal[n_ch]:
            diff += 1
        if diff <= limit and (n_ch < len(start) - 1) and (n_ch < len(goal) - 1):
            return find_diff(n_ch + 1, diff)
        return diff

    a = find_diff(0, 0)
    b = abs(len(goal) - len(start))
    return a + b


    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # BEGIN PROBLEM 7
    if len(start)== 0 or len(goal)== 0:
        return abs(len(start) - len(goal))

    elif start[0] == goal[0]:
        return edit_diff(start[1:], goal[1:], limit)

    elif limit < 0:
        return 1

    else:
        add_diff = 1 + edit_diff(start, goal[1:], limit - 1)
        remove_diff = 1 + edit_diff(start[1:], goal, limit - 1)
        substitute_diff = 1 + edit_diff(start[1:], goal[1:], limit - 1)

        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM 7


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    crct, totl = 0,0
    n_player = 0

    while n_player < len(typed):
        if prompt [n_player] == typed [n_player]:
            crct += 1
            n_player += 1
        else:
            n_player += len(typed)

    progress = crct / len(prompt)
    x = {'id': id, 'progress': progress}
    send(x)
    return progress
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    player_set, n, new_lst, word_lst = [] , 1, [], [] # variables later used

    for x in word_times :
        while n <= n_words:
            time = elapsed_time(x[n]) - elapsed_time(x[n-1])
            player_set = player_set + [time, word(x[n])]
            n += 1
        other_plyr_set = player_set[::2]
        n = 1  # "n" is set to 1 for process to repeat
        new_lst += [player_set]
        word_lst += other_plyr_set
        player_set = []
    n,j = 0,0      # j and n are both counter variables

    while n != n_words  : #  sets slower times to 0.0
        all_times = (word_lst[n ::n_words])
        fast_time = min(all_times)
        n += 1
        for x in new_lst :
            if x[j] + margin  > fast_time  and x[j] - margin  > fast_time  :
                x[j], x[j+1] = 0.0, 0.0
            else:
                x[j] = 0.0
        j = j + 2

    for x in new_lst: # Removes 0.0 and leaves fastest times
        while 0.0 in x:
            x.remove (0.0)
    return new_lst



    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = True # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
