'''
This is the a test file, designed to case-by-case tests for each of the various functions
in tweet analyzer. Needs to still download a file to actaully test the various functions.
For now, this will just prints out the result of the various tests to the terminal.

'''

import tweet_analyzer as ta

test_tweet_1 = "I really hate the new stadium name #herewego  #Steelers"
test_tweet_2 = "Ungo youtube youtube YouTube"
test_tweet_3 = "using the fact that john lennonâ€™s murderer was inspired by the catcher in the rye as why the book sucks is sooo not woke. anyone with integrity should want to kiII john lennon. I would like to kiII john lennon. tell me you wouldnâ€™t like to kiII john lennon"
test_tweet_4 = "Most people who vocalize their weird hate for CATCHER IN THE RYE are too stupid to pour piss out of a boot with the instructions on the heel. If they could write anything better, they would. Alas, they're barely skilled enough to write IKEA instruction manuals. Pity the clowns."
test_tweet_5 = "@RebelTaxi LMFAAOOOO CATCHER IN THE RYE"

#test filter_words function
print(ta.filter_words(test_tweet_1))
print(ta.filter_words(test_tweet_2))
print(ta.filter_words(test_tweet_3))
print(ta.filter_words(test_tweet_4))
print(ta.filter_words(test_tweet_5))

#test get_adj function
print(ta.get_adj(test_tweet_1))
print(ta.get_adj(test_tweet_2))
print(ta.get_adj(test_tweet_3))
print(ta.get_adj(test_tweet_4))
print(ta.get_adj(test_tweet_5))

#test get_noun function
print(ta.get_noun(test_tweet_1))
print(ta.get_noun(test_tweet_2))
print(ta.get_noun(test_tweet_3))
print(ta.get_noun(test_tweet_4))
print(ta.get_noun(test_tweet_5))

#test get_verb function
print(ta.get_verb(test_tweet_1))
print(ta.get_verb(test_tweet_2))
print(ta.get_verb(test_tweet_3))
print(ta.get_verb(test_tweet_4))
print(ta.get_verb(test_tweet_5))

