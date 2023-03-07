#!/usr/bin/python3
# Everett Reynolds
# Eliza Chat Bot
import math
from math import sqrt 
import sys
import random
import os
import re



swapDiction = {
    "i":"you",
    "you":"me",
    "you":"i",
    "me":"you",
    "am":"are",
    "are":"am",
    "my":"your",
    "your":"my",
    "yours":"mine",
    "mine":"yours",
    "are":"am",
    "am":"are"
}

responseDictionary = [ # multi dimensional List
    [r'.* (always).*',
    [
        "Can you think of a specific example?"
    ]],
    [r'.* (because).*',
     [
         "Is that the real reason?"
     ]],
    [r'.* (sorry).*',
      [
          "Please don't apologize.",
          "Are you really sorry?"
      ]],
    [r'.* (maybe).*',
        [
            "You don't seem very certain."
        ]],
     [r'i think (.*)',
        [
            "Do you really think so?"
        ]],
    [r'.* (you).*',
        [
            "We were discussing you, not me."
        ]],
    [r'.* (yes).*',
        [
            "Why do you think so? ",
            "You seem quite positive."
        ]],
    [r'.* (no).*',
        [
            "Why not?",
            "Are you sure? "
        ]],
    [r'(?i)I am(.*)',
        [
            "I am sorry to hear you are %s.",
            "How long have you been %s? ",
            "Do you believe it is normal to be %s?",
            "Do you enjoy being %s? "
        ]],
    [r'i feel (.*)',
        [
            "Tell me more about such feelings.",
            "Do you often feel %s? ",
            "Do you enjoy feeling %s?",
            "Why do you feel that way?"
        ]],
    [r'.* (family|mother|mom|father|dad|sister|brother|husband|wife).*',
        [
            "Tell me more about your family.",
            "How do you get along with your family?",
            "Is your family important to you?"
        ]],
    [r'.* (dream|nightmare|bad dream|good dream).*',
        [
            "What does that dream suggest to you?",
            "Do you dream often?",
            "What persons appear in your dreams?",
            "Are you disturbed by your dreams?",
            "Do you remember your dream?"
        ]],
    [r'.* (love|hate|like|loath|despise|adore).*',
        [
            "Why do you feel this way?",
            " What do you %s about this?"
        ]],
    [r'i cannot compete (.*)|i can\'t compete (.*)',
        [
            "Why can't you compete with this obstacle?",
            "What's stopping you from competing with great vengence and fury?"
        ]],
    [r'(.*)',
        [
            "What does that suggest to you?",
            "I see.",
            "I'm not sure I understand you fully.",
            "Can you elaborate?",
            "That is quite interesting."
        ]]
]

#*def swap(pro):
    #if pro is not None:
        #sent = pro.split()
        #newSent = []
        #for x in sent:
def swap(pro):
    pieces = pro.lower().split()
    for x,word in enumerate(pieces): # This is a better way to do it than a for x in range() for loop, allows for position and value to referenced at same time
        if word in swapDiction:
            pieces[x] = swapDiction[word]
    return " ".join(pieces)

#def parse(sentence):
 #   for strings in responseDictionary: 
  #      entry = re.match(strings, sentence.rstrip(".!?").lower())
   #     if entry:
    #        if strings[0] > len(strings) - 1:
     #           strings[0] = 1
      #      foundSentence = strings[ string[0] ]
       #     strings[0] = strings[0] + 1
        #    return foundSentence.format( * [ swap(pro) for pro in entry.groups() ] ) # returns correct formatted sentence with pronouns swapped where appropriate
def parse(sentence):
    for index, strings in enumerate(responseDictionary):
        pattern = strings[0]
        #print(pattern)
        entry = re.match(sentence, sentence.rstrip(".!").lower())
        if entry:
            foundSentence = strings[random.randrange(0,len(strings))]
            #print(foundSentence)
            for sentences in entry.groups():
                return foundSentence.format(* [ swap(sentences) ])

def main():
    exitClause = ("Bye" , "bye", "Goodbye", "goodbye")
    print("I'm Eliza, Your Favorite Chatbot Psychologist.\n What's Your Name?")
    name = input("- ")
    nameParse = name.split()
    userName = nameParse[-1] # Assumes the last word entered is the name of the person using the bot
    print("Hello " + userName + ". It's a Fantastic Day Today, and I hope yours is going as great as you are as a person :)")
    print("The Doctor is Now In Session. \nWhat's on your mind?")
    while True:
        userInput = input("- ")
        if userInput in exitClause:
            print("It Was Nice Chatting! I Hope Your Day is Splendid :)")
            break
        else:
            print(parse(userInput))


if __name__ == "__main__":
    main()