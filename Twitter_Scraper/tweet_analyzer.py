#in order for this to work, need to download nltk 3.5 to computer
#A good reference for the API i am using:
#https://realpython.com/nltk-nlp-python/
import tweepy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


'''
returns filtered dictionary of all words in the tweet
For example, the code:
test_tweet_1 = "I really hate the new stadium name #herewego  #Steelers"
filter_words(test_tweet_1)

returns {'really': 1, 'hate': 1, 'new': 1, 'stadium': 1, 'name': 1, '#herewego': 1, '#steelers': 1}

'''
def filter_words(tweet_content):
    potential_words_list = tweet_content.split()
    
    stop_words = set(stopwords.words("english"))
    dict_words = {}
    for word in potential_words_list:
        word = word.lower()
        
        # filters out unwanted words in tweets
        if word in stop_words:
            continue
        if word not in dict_words:
            dict_words[word] = 0
        dict_words[word] = dict_words[word] + 1
    
    return dict_words

'''
returns list of adjectives in the tweet
For example, the code:
test_tweet_1 = "I really hate the new stadium name #herewego  #Steelers"
filter_words(test_tweet_1)

returns 
returns {'new': 1}
'''

'''
filters content in tweet, then analyzes content and 
returns a list of adjectives 
O(n) runtime?(find runtime of various functions) 
'''
def get_adj(tweet_content):
    potential_words_list = tweet_content.split()
    
    #dictionary of adjectives
    dict_adj = {}
    
    #returns dictionary of all wordsand there types
    #Key is the word, and content is the type of the word
    #Example {'Name', 'NN'}
    words = word_tokenize(tweet_content)
    words = nltk.pos_tag(words)

    for word, type in words:
        if type == 'JJ':
            if word not in dict_adj:
                dict_adj[word] = 0
            dict_adj[word] = dict_adj[word] + 1
            
    return dict_adj

'''
filters content in tweet, then analyzes content and 
returns a list of nouns
O(n) runtime?(find runtime of various functions) 
'''
def get_noun(tweet_content):
    potential_words_list = tweet_content.split()
    
    #dictionary of adjectives
    dict_noun = {}
    
    #returns dictionary of all wordsand there types
    #Key is the word, and content is the type of the word
    #Example {'Name', 'NN'}
    words = word_tokenize(tweet_content)
    words = nltk.pos_tag(words)

    for word, type in words:
        if type == 'NN':
            if word not in dict_noun:
                dict_noun[word] = 0
            dict_noun[word] = dict_noun[word] + 1
            
    return dict_noun

'''
filters content in tweet, then analyzes content and 
returns a list of verbs
O(n) runtime?(find runtime of various functions) 
'''
def get_verb(tweet_content):
    potential_words_list = tweet_content.split()
    
    #dictionary of adjectives
    dict_verb = {}
    
    #returns dictionary of all wordsand there types
    #Key is the word, and content is the type of the word
    #Example {'Name', 'NN'}
    words = word_tokenize(tweet_content)
    words = nltk.pos_tag(words)

    for word, type in words:
        if type == 'VB':
            if word not in dict_verb:
                dict_verb[word] = 0
            dict_verb[word] = dict_verb[word] + 1
            
    return dict_verb


