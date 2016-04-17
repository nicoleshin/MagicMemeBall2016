from flask import Flask, request, render_template
import random
import cgi
import os

#from app import app
app = Flask(__name__)

yesno = ['does', 'did', 'do', 'has', 'have', 'had', 'can', 'could', 'would', 'should', 'will', 'shall', 'is', 'was']
firstWords = ['does','which','why','who','where','when','how','what','advice']

polarL = os.listdir("static/memes/polar")
whichL = os.listdir("static/memes/which")
whyL = os.listdir("static/memes/why")
whoL = os.listdir("static/memes/who")
whenL = os.listdir("static/memes/when")
whereL = os.listdir("static/memes/where")
howL = os.listdir("static/memes/how")
whatL = os.listdir("static/memes/what")

adviceL = os.listdir("static/memes/advice")

def questionWord(ques):
   ques = ques.lower()
   fun = ques.split(' ')
   if fun[0] != 'in':
       return fun[0]
   else:
       return fun[0] + fun[1]

def choose(memes):
    return random.choice(memes)

def adviceImage():
    return '../static/memes/advice/' + choose(adviceL)

def quesImg(word):
    path = '../static/memes/'
    if questionWord(word) == 'what':
        path += 'what/' + choose(whatL)
    elif questionWord(word) == 'who' or questionWord(word) == 'whose':
        path += 'who/' + choose(whoL)
    elif questionWord(word) == 'which':
        path += 'which/' + choose(whichL)
    elif questionWord(word) == 'why':
        path += 'why/' + choose(whyL)
    elif questionWord(word) == 'where':
        path += 'where/' + choose(whereL)
    elif questionWord(word) == 'when':
        path += 'when/' + choose(whenL)
    elif questionWord(word) == 'how':
        path += 'how/' + choose(howL)
    elif questionWord(word) in yesno:
        path += 'polar/' +  choose(polarL)
    else:
        return 'fuqu'
    return path

def getImage(req):
    try:
        currPath = ''
        failsafe = []
        print req
        if request.method == "POST":
            form = request.form
            unenlightened = form["question"]
            currPath = quesImg(unenlightened)
        if currPath != 'fuqu' and currPath != '':
            print currPath
            return currPath
        else:
            for i in range(20):
                failsafe.append(quesImg(choose(firstWords)) + ' ')
            print failsafe
            return choose(failsafe)
    except:
        print 'except'
        return "../static/memes/advice/getRekt.jpg"

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('questions.html')

@app.route('/answers', methods=['GET','POST'])
@app.route('/answers/', methods=['GET','POST'])
def answers():
    req = request.method
    return render_template('answer.html', image=getImage(req))

@app.route('/advice')
@app.route('/advice/')
def advice():
    return render_template('advice.html')

@app.route('/advisory')
@app.route('/advisory/')
def advisory():
    return render_template('answer.html', image=adviceImage())

if __name__ == "__main__":
    app.run()
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
