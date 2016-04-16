#!usr/bin/python

import random
import cgi

print 'content-type: text/html'
#yes/no: does, has, can, shall, will, is, was
#which
#why
#who/whose
#where
#when
#how
#what
#advice

yesno = ['does', 'did', 'do', 'has', 'have', 'had', 'can', 'could', 'would', 'should', 'will', 'shall', 'is', 'was']

def questionWord(ques):
   ques.split(' ')
   if split[0] != 'in':
       return split[0]
   else:
       return split[0] + split[1]

def choose(memes):
    return random.choice(memes)

def image():
    form = cgi.FieldStorage()
    unenlightened = form.getvalue('question')
    if questionWord(unenlightened) == 'what':
        return 0
    if questionWord(unenlightened) == 'who' or questionWord(unenlightened) == 'whose':
        return 1
    if questionWord(unenlightened) == 'which':
        return 2
    if questionWord(unenlightened) == 'why':
        return 3
    if questionWord(unenlightened) == 'where':
        return 4
    if questionWord(unenlightened) == 'when':
        return 5
    if questionWord(unenlightened) == 'how':
        return 6
    if questionWord(unenlightened) in yesno:
        return 7
    return 8
