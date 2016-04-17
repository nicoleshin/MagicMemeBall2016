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

def htmlPrint(img):
    print '''<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>

        <title>Magic Meme Ball</title>
        <link href="materialize/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons"rel="stylesheet">
         <style>
            body {
                width: 100%;
                height: 100%;
                color: white;
                background-color: black;
            }
            #text {
                padding-left: 200px;
                padding-right: 200px;
            }
            ::-webkit-input-placeholder { /* WebKit, Blink, Edge */
                color: gray;
            }
            :-moz-placeholder { /* Mozilla Firefox 4 to 18 */
                color: gray;
                opacity:  1;
            }
            ::-moz-placeholder { /* Mozilla Firefox 19+ */
                color: gray;
                opacity:  1;
            }
            :-ms-input-placeholder { /* Internet Explorer 10-11*/
                color: gray;
            }
        </style>
    </head>
    <body>
        <img src=''' + img + '''
        <div class="row center">
            <a href="question.html"><button class="btn waves-effect waves-light"
                    id="button"  type="button">More answers...</button></a>
        or
            <a href="advice.html"><button class="btn waves-effect waves-light"
                    id="button" type="button">More advice...</button></a>
        </div>
    </body>
</html>
'''

print image('what ')
print image('fuqery ')
