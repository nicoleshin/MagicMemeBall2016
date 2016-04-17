from flask import Flask, render_template
import random
import cgi
import os

#from app import app
app = Flask(__name__)

yesno = ['does', 'did', 'do', 'has', 'have', 'had', 'can', 'could', 'would', 'should', 'will', 'shall', 'is', 'was']
firstWords = ['does','which','why','who','where','when','how','what','advice']

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

def adviceImage(string):
    return 'static/memes/advice/' + choose(advice)

def quesImg(word):
    path = 'static/memes/'
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

def getImage():
    form = cgi.FieldStorage()
    failsafe = []
    if form.getvalue('question'):
        unenlightened = form.getvalue('question')
        currPath = quesImg(unenlightened)
    else:
        currPath = adviceImage()
    if currPath != 'fuqu':
        return currPath
    else:
        for i in range(20):
            failsafe.append(correctImg(choose(firstWords)) + ' ')
        return choose(failsafe)

@app.route('/')
def index():
    return render_template('questions.html')

@app.route('/answers')
@app.route('/answers/')
def answers():
    return render_template('answer.html', image=getImage())

@app.route('/advice')
@app.route('/advice/')
def advice():
    return render_template('advice.html')

if __name__ == "__main__":
    app.run()
    app.debug=True
    app.run(host='0.0.0.0', port=5000)