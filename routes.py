#<input type = '<type>' name = '<name>' />
#need cover page to link to program
#need page for input
#need page to use input and output answer
#need page to give incorrect answer

from flask import Flask, url_for, request, render_template
from app import app
import weaponcreation

#initial page/server-side interaction
@app.route('/')
def commence():
    #expect to make an html file for the first page like the rest.
    return render_template('AnswerQuestion.html')

#second page
@app.route('/GeneratePhrase', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('CreateQuestion.html')
    elif request.method == 'POST':
        answer = request.form['title']
        finish = weaponcreation.creation_generation(answer)
        return render_template('CreatedQuestion.html', finish = finish)
    else:
        shutdown_server()
        return('Server Shutting down...')
    

    
