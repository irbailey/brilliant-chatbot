#!/usr/bin/env python
# coding: utf-8
# # Basic ChatBot
# 
# Based on tutorials on using n-gram techniques to implement simple chatbots on Brilliant.org


# Dependencies
import random
import Brain
import Bot as ro
import sys

# The list of filenames corresponding to the text files (books) which the bot will read
datadir="data/"
books = [datadir + book for book in ["book1.txt","book2.txt","book3.txt","book4.txt", "book5.txt", "book6.txt", "book7.txt", "book8.txt", "book9.txt", "book10.txt", "book11.txt", "book12.txt", "book13.txt", "book14.txt"] ]        

# The list of random seeds to be iterated over when generating the bot's responses
seeds=[65,754,34,23,5645]

# The size of the window used in the bot's ngram brain (nwin-1 words of context + 1 word of response)
nwin=4

# The number of words of output to be generated in each response
noutput=100

# The start of the bot's sentence (obtain from command line)
mywords=""
for arg in sys.argv[1:]:
    mywords+=arg+" "
mywords=mywords.strip()
    
print("Number of words of context:", nwin-1)

#Create a brain
brain=Brain.NGram()
brain.set_len(nwin)

# Give the brain to a bot
sam=ro.Bot("Sam", brain)

# Teach the bot
sam.read(books)

# Generate responses from the bot
for seed in seeds:
    
    print("initial words: ", mywords)
    print("Using seed:", seed)
    random.seed(seed)
    print(sam.respond(mywords.lower(),noutput))
    print()


