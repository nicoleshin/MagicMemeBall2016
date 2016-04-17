#!usr/bin/python

import random
import cgi
import os

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
firstWords = yesno + ['which','why','who','whose','where','when','how','what','advice']

polar = os.listdir("memes/polar")
which = os.listdir("memes/which")
why = os.listdir("memes/why")
who = os.listdir("memes/who")
when = os.listdir("memes/when")
where = os.listdir("memes/where")
how = os.listdir("memes/how")
what = os.listdir("memes/what")

advice = os.listdir("memes/what")

def questionWord(ques):
   ques = ques.lower()
   fun = ques.split(' ')
   if fun[0] != 'in':
       return fun[0]
   else:
       return fun[0] + fun[1]

def choose(memes):
    return random.choice(memes)

def correctImg(word):
    path = 'memes/'
    if questionWord(word) == 'what':
        path += 'what/' + choose(what)
    elif questionWord(word) == 'who' or questionWord(word) == 'whose':
        path += 'who/' + choose(who)
    elif questionWord(word) == 'which':
        path += 'which/' + choose(which)
    elif questionWord(word) == 'why':
        path += 'why/' + choose(why)
    elif questionWord(word) == 'where':
        path += 'where/' + choose(where)
    elif questionWord(word) == 'when':
        path += 'when/' + choose(when)
    elif questionWord(word) == 'how':
        path += 'how/' + choose(how)
    elif questionWord(word) in yesno:
        path += 'polar/' +  choose(polar)
    else:
        return 'fuqu'
    return path

def image(string):#():
#    form = cgi.FieldStorage()
#    unenlightened = form.getvalue('question')
    failsafe = []
    currPath = correctImg(string)#(unenlightened)
    if currPath != 'fuqu':
        return currPath
    else:
        for i in range(20):
            failsafe.append(correctImg(choose(firstWords)) + ' ')
        return choose(failsafe)

print image('what ')
print image('fuqery ')
