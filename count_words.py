# !/usr/bin/env python
# -*- coding: UTF-8 -*-

def count_words(text):
    '''Turns the text into a dictionary, where keys are the words that occur \
       in the text and their values mean how many times they occur there.'''
    text = text.lower()
    text = text.encode('utf-8')
    
    not_allowed = ['.', ',', ':', ';', '?', '!', '"', '„', '“', '”', '@', '$', 
                   '&', '©', '%', '#', '/', '-', '–', '—', '=', '+', '<', '>', 
                   '(', ')', '~', '»', '«', '{', '}', '[', ']', '§', '€', '…', 
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'d", '’d', 
                   '’ll', '‘', '*']
    negatives = {'isn’t': 'is not', 'don’t': 'do not', 'doesn’t': 'does not', 'can’t': 'can not', 
                 'haven’t': 'have not', 'hasn’t': 'has not', 'hadn’t': 'had not','wasn’t': 'was not',
                 'didn’t': 'did not', 'won’t': 'will not', 'wouldn’t': 'would not',
                 'couldn’t': 'could not', 'shouldn’t': 'should not', 'mustn’t': 'must not'}
    to_be = [' am ', "'m", '’m', ' are ', "'re", '’re', ' is ',"'s", '’s', ' was ', ' were ', 
             ' been ', ' being ']
    to_do = [' did ', ' does ', ' doing ', ' done ']
    to_have = [' has ', ' had ', ' having ', '’ve', "'ve"]
    
    
    for char in not_allowed:
        text = text.replace(char, ' ')
    for n in negatives:
        text = text.replace(n, negatives[n])
    for be in to_be:
        text = text.replace(be, ' be ')
    for do in to_do:
        text = text.replace(do, ' do ')
    for have in to_have:
        text = text.replace(have, ' have ')
    text = text.replace('could', ' can ')
    

    word_list = text.split()
    words = {}

    for word in word_list:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1 
    
    personals = {'I': ['i', 'i', 'me', 'mine', 'my'], 'you': ['your', 'yours'], 'she': ['her', 'hers'], 
                 'he': ['his', 'him'], 'it': ['its'], 'we': ['us', 'our', 'ours'], 
                 'they': ['them', 'their', 'theirs']} 
    for pronoun in personals:
        for word in personals[pronoun]:
            if word in words:
                if pronoun in words:
                    words[pronoun] += words[word]
                else:
                    words[pronoun] = words[word]
                del words[word]
    
    return words

def count_all_words(dictionary):
    total_words = 0
    for word in dictionary:
        total_words += dictionary[word]
    return total_words


import operator

def order(dictionary):
    '''Make an ordered list of the words by their occurence'''
    total_words = count_all_words(dictionary)
    sorted_list = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    for word in sorted_list:
        occ = word[1]
        percentage = round(100.0*occ/total_words, 4)
        sorted_list[sorted_list.index(word)] = sorted_list[sorted_list.index(word)] + ((str(percentage)),)
    return sorted_list


def most_common_words(dictionary, percentage):
    sorted_list = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    most_common = []
    count_perc = 0
    total_words = count_all_words(dictionary)
    for word in sorted_list:
        most_common.append(word[0])
        occ = word[1]
        count_perc += 100.0*occ/total_words
        if count_perc >= percentage:
            break
    return most_common



