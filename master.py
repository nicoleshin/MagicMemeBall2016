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
        return choose(what)
    if questionWord(unenlightened) == 'who' or questionWord(unenlightened) == 'whose':
        return choose(who)
    if questionWord(unenlightened) == 'which':
        return choose(which)
    if questionWord(unenlightened) == 'why':
        return choose(why)
    if questionWord(unenlightened) == 'where':
        return choose(where)
    if questionWord(unenlightened) == 'when':
        return choose(when)
    if questionWord(unenlightened) == 'how':
        return choose(how)
    if questionWord(unenlightened) in yesno:
        return choose(polar)
    return chooose(polar + which + why + who + when + where + how + what + advice)
